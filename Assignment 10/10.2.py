import requests
API_KEY = "6fff3f688ff3e025637ba2174dd75a44"
city = input("Enter municipality name: ")
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}
response = requests.get(url, params=params)
data = response.json()
if response.status_code == 200:
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    print("Weather:", description)
    print("Temperature:", temperature, "°C")
else:
    print("Error:", data.get("message", "Something went wrong"))