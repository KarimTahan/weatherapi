from win10toast import ToastNotifier
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import json

scheduler = BlockingScheduler()
api_key = "insert-key-here"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
interval = 1

def weather_check():
    city_name = "Ottawa"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    toaster = ToastNotifier()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_temperature = round(current_temperature - 273.15)

        feels_like = y["feels_like"]
        feels_like = round(feels_like - 273.15)

        z = x["weather"]
        weather_description = z[0]["description"]

        toaster.show_toast("Weather Report: " + city_name, "Tempearture = " + str(current_temperature) + "*C\nFeels like  = " + str(feels_like) + "*C\nDescription = " + str(weather_description) + "\nNext Update in: " + str(interval) + " hour(s)")

    else:
        print("Nothing dummy")

scheduler.add_job(weather_check, 'interval', hours=interval)
scheduler.start()
