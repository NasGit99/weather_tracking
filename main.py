import requests 
import config

#Find Geolocation to retrieve Latitude and Longitude

def find_geolocation():
    while True:
        city_name = 'New York'
        state_code = 'NY'
        country_code = 'USA'
        limit = 1

        api_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={config.api_key}"
        response = requests.get(api_url)
        
        if response.status_code != 200:
            print("Valid")
        elif response.status_code == 200:
            data = response.json()
            break    

    return data

def find_current_city():
        
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&appid={config.api_key}"

    response = requests.get(api_url)

    data = response.json()

    return data


for i in find_geolocation():
        city_lat = (i['lat'])
        city_lon = (i['lon'])

find_geolocation()



