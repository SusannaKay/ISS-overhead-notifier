import requests
import datetime as dt

MY_LAT = 41.902782
MY_LONG = 12.496365

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

#funziona che ritorna true o false se la mia posizione è nel range +-5 di iss latitude

API_URL = "https://api.sunrise-sunset.org/json"

params = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted": 0
}

response = requests.get(API_URL, params= params)
response.raise_for_status()
data = response.json()
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])

today_hour = dt.datetime.now().hour
print(sunset)
print(today_hour)




#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.