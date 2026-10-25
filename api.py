from datetime import datetime, timezone
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=24.86&longitude=67.01&current_weather=true"
data = requests.get(url, timeout=30).json()
temp = data["current_weather"]["temperature"]
wind = data["current_weather"]["windspeed"]

now = datetime.now(timezone.utc).isoformat(timespec="seconds")
with open("weather_log.csv", "a") as f:
    f.write(f"{now},{temp},{wind}\n")