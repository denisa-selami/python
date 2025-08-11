mimport requests
from datetime import datetime

MY_LAT = 41.1533
MY_LONG = 20.1683

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
        MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = datetime.utcnow().hour

    
    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True
    return False