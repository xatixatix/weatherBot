import requests

async def get_weather_data(location, api_key):
    response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no')
    data = response.json()
    print(f'{data}')
    return data
