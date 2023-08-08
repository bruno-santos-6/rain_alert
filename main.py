import requests

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

weather_list = [True for hour_data in weather_slice if hour_data["weather"][0]["id"] < 700]

if weather_list:
    print("Bring an Umbrella.")
