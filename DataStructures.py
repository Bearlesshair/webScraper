class Car:
    def __init__(self, car_data):
        self.listing_id = car_data['listingId']
        self.stock_type = car_data['stockType']
        self.make = car_data['make']
        self.make_id = car_data['makeId']
        self.model = car_data['model']
        self.model_id = car_data['modelId']
        self.year = car_data['year']
        self.trim = car_data['trim']
        self.body_style = car_data['bodyStyle']
        self.private_seller = car_data['privateSeller']
        self.price = car_data['price']
        self.mileage = car_data['mileage']
        self.vin = car_data['vin']
        self.certified = car_data['certified']
        self.seller = Seller(seller_data=car_data['seller'])


class Seller:
    def __init__(self, seller_data):
        self.id = seller_data['id']
        self.name = seller_data['name']
        self.phone_number = seller_data['phoneNumber']
        self.distance_from_search_zip = seller_data['distanceFromSearchZip']
        self.customer_id = seller_data['customerId']
        self.display_label = seller_data['sellerDisplayLabel']
        self.address = seller_data['streetAddress']
        self.city = seller_data['city']
        self.state = seller_data['state']


if __name__ == "__main__":
    test_car_data = {'type': 'inventory', 'detail': 'searchResults', 'listingId': 776981381, 'stockType': 'Used',
               'make': 'Mazda', 'makeId': 20073, 'model': 'MX-5 Miata', 'modelId': 21460, 'year': 2005, 'trim': 'LS',
               'bodyStyle': 'Convertible', 'customerId': 5383201, 'seller':
                   {'id': 49146288, 'name': 'St George Auto Brokers', 'phoneNumber': '4074340075', 'phoneNumber2': None,
                    'distanceFromSearchZip': 1307, 'customerId': 5383201, 'sellerDisplayLabel': 'Dealer',
                    'streetAddress': '6436 E Colonial Dr', 'city': 'Orlando', 'state': 'FL', 'truncatedDescription': '',
                    'rating': 2.5, 'reviewCount': '2', 'dealerChatProvider': 'Dealer Inspire',
                    'hasCpoShowroomEnabled': False, 'formattedPhoneNumber': '(407) 434-0075',
                    'formattedPhoneNumber2': None},
               'certified': False, 'privateSeller': False, 'price': 2890, 'mileage': 171138, 'vin': 'JM1NB353350410478',
               'priceBadge': ''}
    testCar = Car(car_data=test_car_data)
    print(testCar.mileage)


