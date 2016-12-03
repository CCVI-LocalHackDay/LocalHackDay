from twitter import *
import config
twitter = Twitter(auth=OAuth(config.twitterKeys["accessKey"], config.twitterKeys["accessSecret"], config.twitterKeys["consumerKey"], config.twitterKeys["consumerSecret"]))
#query = twitter.search.tweets(q="music", geocode = "", count=100, max_id=None, until="2016-10-22")
query = twitter.search.tweets(q = "lazy dog", count = 100)
for result in query["statuses"]:
        # -----------------------------------------------------------------------
        # only process a result if it has a geolocation
        # -----------------------------------------------------------------------
        user = result["user"]["screen_name"]
        text = result["text"]
        text = text.encode('ascii', 'replace')
        print(text)