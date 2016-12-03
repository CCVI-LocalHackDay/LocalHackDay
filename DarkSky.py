from forecastiopy import *
import config
import requests
import json

send_url = "http://freegeoip.net/json"
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']

Location = [lat, lon]
fio = ForecastIO.ForecastIO(config.darkSkyKey, latitude=Location[0], longitude=Location[1])
current = FIOCurrently.FIOCurrently(fio)
print('Temperature:', current.temperature)
print('Precipitation Probability:', current.precipProbability)
