from twitter import *
import config
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from forecastiopy import *
Lisbon = [38.7252993, -9.1500364]
handle  = "realdonaldtrump"
def getTweetValues(handle):
    #fio = ForecastIO.ForecastIO(config.darkSkyKey, latitude=Lisbon[0], longitude=Lisbon[1])
    #current = FIOCurrently.FIOCurrently(fio)
    #print('Temperature:', current.temperature)
    twitter = Twitter(auth=OAuth(config.twitterKeys["accessKey"], config.twitterKeys["accessSecret"], config.twitterKeys["consumerKey"], config.twitterKeys["consumerSecret"]))
    #query = twitter.search.tweets(q="music", geocode = "", count=100, max_id=None, until="2016-10-22")
    #query = twitter.search.tweets( count = 100, until="2016-11-25")
    results = twitter.statuses.user_timeline(screen_name = handle, count = 100)
    # print(len(results))
    sScores = []
    tweets = []
    dates = []
    byDate = {}
    for result in results:
        text = result["text"]
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(text)
        curDate = result["created_at"]
        print(curDate)
        curDate = curDate[0:11]+curDate[26:30]
        print(curDate)
        if curDate in dates:
            byDate[curDate].append(ss)
        else:
            score = ss["compound"]
            byDate[curDate] = [score]
    print(byDate)
    # for result in results:
    #     curDate = result["created_at"])
    #     sid = SentimentIntensityAnalyzer()
    #     # print(sentence)
    #
    #     user = result["user"]["screen_name"]
    #     text = result["text"]
    #     #text = text.encode('ascii', 'replace')
    #     ss = sid.polarity_scores(text)
    #     sScores.append(ss["compound"])
    #     # print(text)
    #     # print(ss)
    #     tweets.append(text)
    #     dates.append(result["created_at"])
    return{"sScores":sScores, "tweets":tweets, "dates":dates}
print(getTweetValues("realdonaldtrump"))