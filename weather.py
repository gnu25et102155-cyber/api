import requests

API_KEY = "91e828401c93afe11fefff459b786295"  # Replace with your actual API key from openweathermap.org
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("\n📍 Location:", data["name"], ",", data["sys"]["country"])
    print("🌡 Temperature:", data["main"]["temp"], "°C")
    print("☁ Weather:", data["weather"][0]["description"])
    print("💧 Humidity:", data["main"]["humidity"], "%")
    print("💨 Wind Speed:", data["wind"]["speed"], "m/s")
else:
    print("❌ Error:", data.get("message", "Something went wrong"))