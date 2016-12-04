import datetime
from datetime import date
from tkinter import *
from geopy.geocoders import Nominatim
from matplotlib import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import subplots, xlabel
from numpy import *
from yahoo_finance import Share

import backend


def get_between_days(startdate, enddate):
    d1 = startdate.split('-')
    d2 = enddate.split('-')
    d1 = date(int(d1[0]), int(d1[1]), int(d1[2]))
    d2 = date(int(d2[0]), int(d2[1]), int(d2[2]))
    delta = d2 - d1
    return (delta.days)


def get_day_id(list_day):
    new_x = []

    for i in list_day:
        new_x.append(get_between_days(list_day[0], i))

    return (new_x)


def graphTweets(handle):
    dataSetTweetValue = (backend.getTweetValues(handle))
    x = []
    y = []
    keys = []
    for i in dataSetTweetValue:
        keys.append(i)

    keys = sorted(keys)
    # print(keys)
    # print("FRED", get_day_id(keys))
    x_values = get_day_id(keys)
    for i in keys:
        y.append(dataSetTweetValue[i])
    axarr[3].plot(x_values, y)
    return keys[0], keys[-1]


def get_historical_price(startdate, enddate):
    nya = Share('NYA')
    date_adj_close = []
    historical_data = nya.get_historical(startdate, enddate)

    for i in historical_data:
        date_adj_close.append([i['Date'], i['Adj_Close']])

    return date_adj_close[::-1]


def graphStocks(start, end):
    Price = get_historical_price(start, end)
    y_values = []
    x_values = []
    for i in Price:
        x_values.append(i[0])
        y_values.append(i[1])

    x_values = get_day_id(x_values)
    axarr[2].plot(x_values, y_values)
    # canvas.show()


def graphWeather(lat, long, startDate, endDate):
    dates = []
    data = backend.getWeather(lat, long, startDate, endDate)
    maxs = []
    mins = []
    precis = []
    for i in data:
        maxs.append(i[1])
        mins.append(i[0])
        precis.append(i[2])
    graphHum(precis)
    graphTemp(maxs, mins)


def graphTemp(maxi, mini):
    maxs = array(maxi)
    mins = array(mini)
    avg = (maxs + mins) / 2
    axarr[0].plot(maxs)
    axarr[0].plot(mins)
    axarr[0].plot(avg)
    # canvas.show()


def graphHum(hum):
    axarr[1].plot(hum)
    # canvas.show()


def getHandleLocation():
    works = False
    tweetHandle = twitterHandleEntry.get()
    if tweetHandle != "":
        geoL = Nominatim()
        loc = geoL.geocode(location.get())
        if loc is None:
            location.delete(0, END)
            twitterHandleEntry.config(bg="white")
            location.config(bg="red")
        else:
            print(loc)
            print(tweetHandle, loc.latitude, loc.longitude)
            works = True
    else:
        twitterHandleEntry.config(bg="red")
        location.config(bg="white")
        twitterHandleEntry.delete(0, END)
        works = True

    if works:
        location.config(bg="white")
        twitterHandleEntry.config(bg="white")
        startday, endday = graphTweets(tweetHandle)
        # print(startday, endday)
        s = startday.split("-")
        e = endday.split("-")
        # print(s, e)
        for i in range(0, 3):
            s[i] = int(s[i])
            e[i] = int(e[i])

        start_date = datetime.date(s[0], s[1], s[2])
        end_date = datetime.date(e[0], e[1], e[2])
        # print(start_date,end_date)
        labels = list(backend.daterange(start_date, end_date))
        # print("LABEL",labels)
        graphStocks(startday, endday)
        Label(controlP,text=("Start Date: "+startday)).grid(row=1,column=3)
        Label(controlP,text=("End Date: "+endday)).grid(row=2,column=3)
        f.tight_layout()
        graphWeather(loc.latitude, loc.longitude, startday, endday)
        canvas.show()


root = Tk()
use('TkAgg')
root.wm_title("NAME")



x = array([])
y = array([])
f, axarr = subplots(4)

axarr[0].plot(x, y)
axarr[0].set_title('Temperature')
axarr[0].set_ylabel('Degrees Celsius')

axarr[1].scatter(x, y)
axarr[1].set_title('Humidity')
axarr[1].set_ylabel('Humidity')

axarr[2].plot(x, y ** 2)
axarr[2].set_title('Stock Exchange')
axarr[2].set_ylabel('Stocks')

axarr[3].scatter(x, y)
axarr[3].set_title('Happiness')
axarr[3].set_ylabel("Happiness Index")
xlabel(1, text="Days Since Start Day")
canvas = FigureCanvasTkAgg(f, master=root)
f.tight_layout()
canvas.show()

canvas.get_tk_widget().pack(side=TOP, expand=1)

# toolbar = NavigationToolbar2TkAgg(canvas, root)
# toolbar.update()
canvas._tkcanvas.pack(side=TOP, expand=1)

controlP = Frame(root)
controlP.pack(side=LEFT)
Label(controlP, text="Enter Twitter Handle").grid(row=1, column=1)
twitterHandleEntry = Entry(controlP, exportselection=0)
twitterHandleEntry.insert(0, "realdonaldtrump")
twitterHandleEntry.grid(row=1, column=2)
Label(controlP, text="Enter Location").grid(row=2, column=1)
location = Entry(controlP, exportselection=0)
location.insert(0, "382 Cavendish Drive Waterloo Ontario")
location.grid(row=2, column=2)

sub = Button(controlP, text="Entry", command=getHandleLocation)
sub.grid(row=5, column=1)


def _quit():
    root.quit()  # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent


button = Button(controlP, text='Quit', command=_quit)
button.grid(row=5,column=2)

root.protocol("WM_DELETE_WINDOW", _quit)
root.mainloop()
