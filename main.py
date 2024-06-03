import requests
import datetime as dt
import smtplib
from passwords import *
import time

MY_LAT = 41.902782
MY_LONG = 12.496365

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg="Subject:LookUp!\n ISS is about to come!"
        )

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def position_checker():
    return MY_LAT - 5 <= iss_latitude <= MY_LAT +5 and MY_LONG -5<= iss_longitude <= MY_LONG +5



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

while True:
    time.sleep(60)
    if position_checker() and today_hour > sunset or today_hour < sunrise:

        send_email()
    else: 
        print("nessuna notifica")

