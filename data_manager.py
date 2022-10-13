import requests
import pprint
SHEETY_USERS_ENDPOINT= "https://api.sheety.co/ff8553210d7b68f0afc4ac5fb1391d73/flightDeals/users"
SHEETY_ENDPOINT = "https://api.sheety.co/ff8553210d7b68f0afc4ac5fb1391d73/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}


    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        #pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data= {
                "price": {
                    "iataCode" : city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",
                                     json=new_data)

            print(response.text)
    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response= requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data