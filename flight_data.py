class FlightData:

    def __init__(self, price, origin_city, origin_airport,
                 destination_city,destination_airport,out_date, return_date,stop_overs=0, via_city=""):
        self.price = price,
        self.origin_city = origin_city,
        self.origin_airport = origin_airport,
        self.destination_city = destination_city,
        self.destination_airport = destination_airport,
        self.out_date = out_date,
        self.return_date = return_date,
        self.stop_overs = stop_overs,
        self.via_city = via_city

# TEQUILA_API_ENDPOINT = "https://api.tequila.kiwi.com"
# TEQUILA_API_KEY = "5jWeVMiW_GTxc36CUHBOUdDdSzWandXS"
# def search_price(self,city_name):
#
#     SEARCH_ENDPOINT=f"{TEQUILA_API_ENDPOINT}/search"
#     headers= {"apikey": SEARCH_ENDPOINT }
#     query = {
#         "duration" : 1440*7,
#         "cityFrom" : "IST",
#         "cityTo" : city_name,
#         "nights_in_dst_from" : 7,
#         "nights_in_dst_to" : 28,
#         "flight_type" : "round",
#
#     }
#     response=requests.get(url=SEARCH_ENDPOINT,headers=headers, params=query)
#     result=response.json()["search_response"]
#     price=result[0]["price"]
#     return price
#
# departure_time_soonest = datetime.datetime.now()+ datetime.timedelta(days=1)
# departure_time_latest = datetime.datetime.now()+datetime.timedelta(days=180)

