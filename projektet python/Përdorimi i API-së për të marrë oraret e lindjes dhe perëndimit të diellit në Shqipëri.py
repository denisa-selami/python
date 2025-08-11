import requests
from datetime import datetime

MY_LAT = 41.1533
MY_LONG = 20.1683

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(f"Lindja e diellit ne Shqiperi: ora {sunrise}")
print(f"Perëndimi i diellit ne Shqieri: ora {sunset}")
