from forecastiopy import *
import config

Guelph = [43.5230543, -80.24893800000001]
fio = ForecastIO.ForecastIO(config.darkSkyKey, latitude=Guelph[0], longitude=Guelph[1])
current = FIOCurrently.FIOCurrently(fio)
print('Temperature:', current.temperature)
print('Precipitation Probability:', current.precipProbability)
