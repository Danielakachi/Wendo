import requests

api_address='https://api.openweathermap.org/data/2.5/weather?appid=c676d88878693c79b319d82d416591a4&q='

city=input("Enter City Name:")

url=api_address+city

json_data=requests.get(url).json()

formatted_data_weather_describtion=json_data['weather'][0]['main']

formatted_data_temperature_describtion=json_data['main']['temp']



print("weather: "+formatted_data_weather_describtion)
print("Temperature: "+str(formatted_data_temperature_describtion))



