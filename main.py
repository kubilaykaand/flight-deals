# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import data_manager
from flight_search import FlightSearch
import flight_data
from notification_manager import NotificationManager
import datetime

flight_search = FlightSearch()
data_manager = data_manager.DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

origin_city_iata = "LAX"
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
six_months_from_today = datetime.datetime.now() + datetime.timedelta(days=6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(origin_city_iata,
                                         destination["iataCode"],
                                         from_time=tomorrow,
                                         to_time=six_months_from_today
                                         )

    if flight is None:
        continue

    if flight.price[0] < destination["lowestPrice"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Your ticket to {flight.origin_city[0]}-{flight.origin_airport[0]} to {flight.destination_city[0]}-"
        f"{flight.destination_airport[0]}, in {flight.out_date[0]} to {flight.return_date[0]} has reduced to "
        f"${flight.price[0]}"

        if flight.stop_overs[0] > 0:
            message += f"\nFlight has {flight.stop_overs[0]} stop over, via {flight.via_city[0]}."
            print(message)
            notification_manager.send_sms(message)

        link = f"https://www.google.co.uk/flights?hl=enflt={flight.origin_airport}.{flight.destination_airport}."\
                f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        notification_manager.send_emails(emails,message,link)