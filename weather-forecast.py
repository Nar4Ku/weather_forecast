import requests
import json
import datetime

enter = ''

while True:
    enter = input('Welcome to the Weather Forecast program! Type anything to start or (N) to exit')

    if enter.lower() == 'n':
        break

    print('\n\tWeather Forecast\t', datetime.datetime.now())
    city = input('\nType the city...')
    request = requests.get('http://api.openweathermap.org/data/2.5/weather?q='
                       + city +'&appid=23714b176cdc3adf825ba11bee911e31')
    weather = json.loads(request.text)
    print('\nWeather condition:', weather['weather'][0]['main'])
    temperature = (float(weather['main']['temp']) - 273.15)
    print('Temperature: {:.2f} graus C°'.format(temperature))

print('Thank you for using')
