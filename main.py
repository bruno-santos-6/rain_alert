import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os
from dotenv import load_dotenv

# -------------- Exporting Environment Variables --------------
load_dotenv(".env")

# ---------------------- Twilio API Info ----------------------
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_numer = os.getenv("TWILIO_NUMBER")
my_verified_number = os.getenv("MY_TWILIO_VERIFIED_NUMBER")

# --------------- Open Weather Map API Info (OWM) ---------------
api_key = os.environ.get("OWM_API_KEY")
city_latitude = -23.179140
city_longitude = -45.887241
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": city_latitude,
    "lon": city_longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

weather_list = [True for hour_data in weather_slice if hour_data["weather"][0]["id"] > 700]

if weather_list:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
    body = "It's going to rain today. Remember to bring an ☔",
    from_ = twilio_numer,
    to = my_verified_number
    )

    print(message.status)
