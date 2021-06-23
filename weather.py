import requests
from datetime import datetime

api_key = 'a06a711b6177318cfd056d1e0c13c76b'
location = input("Enter the city name -:")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

contry = api_data['sys']['country']
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
mini = ((api_data['main']['temp_min']) - 273.15)
mix = ((api_data['main']['temp_max']) - 273.15)
feels_like = ((api_data['main']['feels_like']) - 273.15)
pressure = api_data['main']['pressure']
hmdt = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
deg = api_data['wind']['deg']
data_time = datetime.now().strftime(" %d %b %Y | %I %M %S %p")

print("----------------------------------------------------------------")
print("Weather stats for - {} || {}".format(location.upper(), data_time))
print("Country Code - :", contry)
print("----------------------------------------------------------------")

print("Current temperature is : {:.2f} deg C".format(temp_city))
print("Current minimum temperature is : {:.2f} deg C".format(mini))
print("Current maximum temperature is : {:.2f} deg C".format(mix))
print("Current temperature feels like : {:.2f} deg C".format(feels_like))
print("Current weather description :", weather_desc)
print("Current humidity :", hmdt, '%')
print("Current wind speed :", wind_speed, 'kmph')
print("Current atm pressure :", pressure, 'hPa')
print("Current wind directon :", deg, '°')