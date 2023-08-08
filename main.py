import requests
from twilio.rest import Client

# ---------------------- Twilio API Info ----------------------
account_sid = "ACc78eb3fbcc26902d3bf7eb22067e69ec"
auth_token = "691f0085ca9cba61f388a623172f250b"
twilio_numer = "+12059527423"
my_verified_number = "+5512996077702"

# ---------------------- Weather API Info ----------------------
angela_api_key = "69f04e4613056b159c2761a9d9e664d2"
api_key = "1122399b2c9eb9402ba15b1f52cb5339"
city_latitude = -23.179140
city_longitude = -45.887241
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": city_latitude,
    "lon": city_longitude,
    "appid": angela_api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

weather_list = [True for hour_data in weather_slice if hour_data["weather"][0]["id"] > 700]

if weather_list:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
    body = "It's going to rain today. Remember to bring an ☔",
    from_ = twilio_numer,
    to = my_verified_number
    )

    print(message.status)
