from twitter import *
import config
import numpy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from forecastiopy import *

def getTweetValues(handle):
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
        #print(curDate)
        curDate = curDate[0:11]+curDate[26:30]
        months = {"Jan":"01", "Feb": "02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10","Nov":"11","Dec":"12"}
        month = months[curDate[4:7]]
        day = curDate[8:10]
        year = curDate[11:15]
        curDate = year+"-"+month+"-"+day
        # print(curDate)
        # print(ss["compound"])
        if curDate in byDate:
            # print("OLOLOLOLOLOOLAOLALLALALALAA")
            byDate[curDate].append(ss["compound"])
        else:
            score = ss["compound"]
            byDate[curDate] = [score]
    for date in byDate:
        byDate[date] = numpy.mean(byDate[date])
        # print(byDate[date])
    # print(byDate)
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
    return byDate
def getWeather(lat, long):
    fio = ForecastIO.ForecastIO(config.darkSkyKey, latitude=Lisbon[0], longitude=Lisbon[1])
    current = FIOCurrently.FIOCurrently(fio)
    print('Temperature:', current.temperature)
if __name__ == '__main__':
    print(getTweetValues("BBCBreaking"))