import requests
import flight_data
import datetime
import notification_manager
class FlightSearch:
    def __init__(self):
        self.API_KEY="ucSC1CgBktgYBtUDrZe0NIW5SuLLtMaN"
        self.fly_data = flight_data.FlightData().flight_data
        self.today = datetime.date.today().strftime("%d/%m/%Y")
        for num in range(len(self.fly_data['cities'])):
            self.city = self.fly_data['cities'][num]
            self.price = self.fly_data['prices'][num]
            self.headers ={
                "apikey":self.API_KEY
            }
            self.params={
                "fly_from":"KRK",
                "fly_to":self.city,
                "date_from":self.today,
                "date_to":'09/07/2024',
                "curr":"PLN"
            }

            self.response = requests.get("https://api.tequila.kiwi.com/v2/search",params=self.params,headers=self.headers)
            self.min_price=(self.response.json()["data"][0]['price'])
            self.fly_date = (self.response.json()["data"][0]["local_departure"])
            if self.min_price < self.price:
                notification_manager.NotificationManager(self.city,self.min_price,self.fly_date)

