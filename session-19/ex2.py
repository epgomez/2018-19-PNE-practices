# Example of getting information about the weather of
# a location

import http.client
import json

# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINTS = ["/api/location/search/?query=", '/api/location/']

city = input('Please, enter the city desired: ')
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

try:
    conn.request(METHOD, ENDPOINTS[0] + city, None, headers)

    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")

    weather = json.loads(text_json)
    woeid = str(weather[0]['woeid'])

    conn.request(METHOD, ENDPOINTS[1] + str(woeid) + '/', None, headers)
    r2 = conn.getresponse()

    print("Response received: ", end='')
    print(r2.status, r2.reason)
    print()

    text_json1 = r2.read().decode("utf-8")
    city_data = json.loads(text_json1)

    conn.close()

    print('The city you have requested is: {}'.format(weather[0]['title']))
    print()
    print('The actual time is: '+ str(city_data['time'].split('T')[1].split('+')[0])[:11])
    print('The temperature is: '+ str(round(city_data['consolidated_weather'][0]['the_temp'],3)))
    print('Sunset will be at: ' + str(city_data['sun_set'].split('T')[1].split('+')[0])[:11])

except IndexError:
    print("\nThe city requested doesn't have an available woeid")