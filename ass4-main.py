import requests

API_KEY = "fd2ea79ca450124eebfd1df53b8d38ef"
city = input("Enter a city to look for the weather: ")
api_url= "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city,API_KEY)
weather_data = requests.get(api_url).json()

try:
    print("The teamprture in {} is {} Celsius. It has {} right now".
          format(city,
                 weather_data['main']['feels_like'],
                 weather_data['weather'][0]['description']))


except KeyError:
    print("Wrong city input")
