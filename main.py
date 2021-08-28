
import requests, json, os, time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() #takes environment variable from .env

api_key = "Paste you API key" 
base_url = "https://api.openweathermap.org/data/2.5/weather?q="

print("Hello!")
time.sleep(0.5)
print("Here You can find weather of your and other cities!")
time.sleep(2)
city_name = input("City Name: ")
complete_url = base_url + city_name + "&appid=" + api_key
response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    pressure = y["pressure"]
    humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print('----'*10)
    print("Location : {} \nTemperature: {:.2f} *C \nDescription: {} \nHumidity: {} \nPressure: {}".format(city_name.capitalize(), (current_temperature - 273), str(weather_description.capitalize()), str(humidity), str(pressure)))
    print('----'*10)
else:
    print("Not Found!")