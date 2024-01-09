import requests
class FlightData:
    def __init__(self):
        self.response = requests.get('https://api.sheety.co/272d5a45db0be49eb0b256d1f75d8139/flightDeals/prices')
        self.data = self.response.json()['prices']
        self.flight_data={
            "cities":[],
            "prices":[]
        }
        for row in self.data:
            self.flight_data['cities'].append(row['iataCode'])
            self.flight_data['prices'].append(row['lowestPrice'])


