import requests

async def get_weather_data(location, api_key):
    response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no')
    data = response.json()
    print(f'{data}')
    return weather_to_string(data)

def weather_to_string(weather_data):
    return (f'At {weather_data["location"]["name"]} '
            f'the temperature is {weather_data["current"]["temp_c"]} C° '
            f'and it feels like {weather_data["current"]["feelslike_c"]} C°. '
            f'you can expect wind gusts of up to {weather_data["current"]["gust_kph"]} kph.')