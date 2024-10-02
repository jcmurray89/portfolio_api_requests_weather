import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"
# https://rapidapi.com/weatherapi/api/weatherapi-com/playground/apiendpoint_bef542ef-a177-4633-aacc-ee9703945037

#querystring = {"q":"53.1,-0.13"}
querystring = {"q": "50317"}
# Valid strings for "q" are (lat, long), city name, Us zip code, UK zip code

headers = {
	"x-rapidapi-key": "9c9078bccdmshfdb7bd6acbb66edp1a009djsn9196a955ff5c",
	"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
}

response2 = requests.get(url, headers=headers, params=querystring)
print(response2.json())

#print(type(response2.json())) # Answer: it is a dictionary

response_dict = response2.json()

for key in response_dict.keys():
    print(key)

place = response_dict['location']['name']

print(place)

weather_temp = response_dict['current']['temp_f']

print(weather_temp)

for key in response_dict['current']:
    print(key)

print("\nNow that we know our opitons, a real function test:\n")

'''
Output: returned weather stats: 

last_updated_epoch
last_updated
temp_c
temp_f
is_day
condition
wind_mph
wind_kph
wind_degree
wind_dir
pressure_mb
pressure_in
precip_mm
precip_in
humidity
cloud
feelslike_c
feelslike_f
windchill_c
windchill_f
heatindex_c
heatindex_f
dewpoint_c
dewpoint_f
vis_km
vis_miles
uv
gust_mph
gust_kph
'''


def weather_statement_maker(weather_api_response, *factors):
    response_dict = weather_api_response.json()
    city = response_dict['location']['name']
    country = response_dict['location']['country']
    print("The current weather in {c}, {u}".format(c = city, u = country), ": \n")
    for factor in factors:
        value = response_dict['current'][factor]
        print("The current {f} is {v}".format(f=factor, v=value))


check_weather = weather_statement_maker(response2, 'temp_f', 'wind_mph', 'humidity', 'cloud')


print(check_weather)