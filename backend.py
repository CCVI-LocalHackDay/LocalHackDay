from twitter import *
import config
from forecastiopy import *
Lisbon = [38.7252993, -9.1500364]
fio = ForecastIO.ForecastIO(config.darkSkyKey, latitude=Lisbon[0], longitude=Lisbon[1])
current = FIOCurrently.FIOCurrently(fio)
print('Temperature:', current.temperature)
twitter = Twitter(auth=OAuth(config.twitterKeys["accessKey"], config.twitterKeys["accessSecret"], config.twitterKeys["consumerKey"], config.twitterKeys["consumerSecret"]))
query = twitter.search.tweets(q="music", geocode = "", count=100, max_id=None, until="2016-10-22")
query = twitter.search.tweets(q = "justin trudeau", count = 100)
for result in query["statuses"]:
        user = result["user"]["screen_name"]
        text = result["text"]
        text = text.encode('ascii', 'replace')
        print(text)