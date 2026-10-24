import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=24.86&longitude=67.01&current_weather=true"
response = requests.get(url)
print(response.status_code)

data = response.json()
print(data["current_weather"]["temperature"])