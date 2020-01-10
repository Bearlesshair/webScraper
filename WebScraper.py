import numpy as np
import DataStructures
import re
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.cars.com/for-sale/searchresults.action/?dealerType=all&mdId=20823&mkId=20017&page=1&perPage=100&rd=99999&searchSource=GN_REFINEMENT&sort=relevance&trId=25362&yrId=39723&yrId=47272&yrId=51683&yrId=56007&zc=55127"
page_match = re.search("&page=(\d+)&", url)
page = int(page_match.groups()[0])
last_page = 0


def next_page(url, page):
    url = re.sub("&page=" + str(page) + "&", "&page=" + str(page + 1) + "&", url)
    return url


cars = []
while page != last_page:
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    type(soup)
    # Extracts the car data
    # text = soup.get_text()
    # print(soup.text)
    all_scripts = soup.find_all('script')
    for script in all_scripts:
        text = str(script)
        # print(text)

        if re.search("CARS\.digitalData\W=\W(.+);", text):
            z = re.search("CARS\.digitalData\W=\W(.+);", text)
            x = z.groups()[0]
            foo = json.loads(x)
            search_info = foo["page"]["search"]
            # print(search_info)
            cars_raw = foo["page"]["vehicle"]
    for car in cars_raw:
        cars.append(DataStructures.Car(car))
    page = search_info['pageNum']
    last_page = search_info['totalNumPages']
    url = next_page(url, page)
print(len(cars))
# print(cars_raw[0])
# print(all_scripts)
a = np.array([[1, 2, 3, 4]])
for car in cars:
    if car.price is None or car.mileage is None:
        continue
    a = np.append(a, [[car.price, car.mileage, car.year, car.listing_id]], axis=0)
a = np.delete(a, 0, axis=0)
print(len(a))
mileage = a[:, 1]
price = a[:, 0]
year = a[:, 2]
mileage_stats = np.array([np.percentile(mileage, q=0), np.percentile(mileage, q=25),
                          np.percentile(mileage, q=50), np.percentile(mileage, q=75),
                          np.percentile(mileage, q=100)])
print("mileage stats:{}".format(mileage_stats))
price_stats = np.array([np.percentile(price, q=0), np.percentile(price, q=25),
                        np.percentile(price, q=50), np.percentile(price, q=75),
                        np.percentile(price, q=100)])
print("price stats:{}".format(price_stats))

price_mileage = np.poly1d(np.polyfit(mileage, price, 1))
price_year = np.poly1d(np.polyfit(year, price, 1))
#plt.plot(mileage, price, 'ro')
#plt.plot(np.unique(mileage), price_mileage(np.unique(mileage)))
#plt.show()
print(price_mileage)
#plt.plot(year, price, 'ro')
#plt.plot(np.unique(year), price_year(np.unique(year)))
#plt.show()
print(price_year)
