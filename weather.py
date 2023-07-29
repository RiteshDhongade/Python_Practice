import requests

api_key = "put api key here"
city = "Nagpur"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"
request = requests.get(url)
json = request.json()
#print(json)
description = json.get("weather")[0].get("description")
print("Today's forcast is", description)
temp_min = json.get("main").get("temp_min")
print("Minimum temperatur is", temp_min)
temp_max = json.get("main").get("temp_max")
print("Maximum temperatur is", temp_max)
coord_lon = json.get("coord").get("lon")
coord_lat = json.get("coord").get("lat")
print(city," longitute is", coord_lon," and latitude is", coord_lat)