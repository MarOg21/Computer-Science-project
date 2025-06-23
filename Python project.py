import requests
# Import required module
# Define the city and API key
city = "Berlin" 
# OpenWeatherMap API key through https://openweathermap.org/api

API_key = "dbb5fa785ccb1575d3676047136288df"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Analyse the JSON response
    data = response.json()
    print("weather is", data["weather"][0]["description"])
    print("current temperature is", data["main"]["temp"])
    print("current temperature feels like is", data["main"]["feels_like"])
    print("current temperature feels like is", data["main"]["humidity"])






    
