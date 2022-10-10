'''
import urllib.request, urllib.parse, urllib.error
import ssl
import re
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

weather = 'https://api.weather.gov/'
func = input('What do you want to do: ')
if func == 'temperature' :
    print('Ex: BOI/0/0')
    location = input('Where are you: ')
    func = 'gridpoints/' + location + '/forecast'

connection = urllib.request.urlopen(weather+func, context=ctx)
data = connection.json()
print(data.read().decode())
'''
'''
import requests

response = requests.get("http://randomfox.ca/floof")
print(response.status_code)
print(response.text) #String
print(response.json()) #Actual JSON DICTIONARY

fox = response.json()
print(fox['image'])
'''






import requests
import json

def call(header,alias) :
    response = requests.get(header+alias)
    data = response.json()
    if alias == points :
        print(header+alias)
        format = data['properties']['forecast']
        reRetrieve = format.replace('"', "")
        print(reRetrieve)
        responseNew = requests.get(reRetrieve)
        dataNew = responseNew.json()
        formatNew = dataNew['properties']['periods'][0]['detailedForecast']
        forecast = formatNew.replace("'", "")
    elif alias == gridpoints :
        format = data['properties']['periods'][0]['detailedForecast']
        forecast = format.replace("'", "")
    if response.status_code == 404 :
        print('Error: 404')
    elif response.status_code == 200 :
        print('Success: 200')
    else :
        print(response.status_code)
        format = 'Could not parse json.'
    print(forecast)

weather = 'https://api.weather.gov/'
func = input('What do you want to do: ')
if func == 'office' :
    print('Ex: TOP/31,80')
    location = input('Where are you: ')
    gridpoints = 'gridpoints/' + location + '/forecast'
    call(weather,gridpoints)
elif func == 'forecast' :
    print('Ex: 43.617,-116.1981')
    location = input('Where are you: ')
    points = 'points/' + location
    call(weather,points)
