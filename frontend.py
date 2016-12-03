from tkinter import *
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import subplots
from numpy import *
from geopy.geocoders import Nominatim
import backend
from datetime import date
from yahoo_finance import Share


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
    # print(dataSetTweetValue)
    x = []
    y = []
    keys = []
    for i in dataSetTweetValue:
        keys.append(i)
    # print("keys", keys)

    keys = sorted(keys)
    # print(keys)
    # print("FRED", get_day_id(keys))
    x_values = get_day_id(keys)
    # print("Values", x_values)
    for i in keys:
        y.append(dataSetTweetValue[i])
    axarr[3].plot(x_values, y)
    # print(y)
    canvas.show()
    print(keys[0], keys[-1])
    return keys[0], keys[-1]


def get_historical_price(startdate, enddate):
    nya = Share('NYA')
    date_adj_close = []
    historical_data = nya.get_historical(startdate, enddate)

    for i in historical_data:
        date_adj_close.append([i['Date'], i['Adj_Close']])

    return date_adj_close[::-1]


def graphStocks(start, end):
    print(start, end)
    Price = get_historical_price(start, end)
    print("Price", Price)
    y_values = []
    x_values = []
    for i in Price:
        x_values.append(i[0])
        y_values.append(i[1])

    x_values = get_day_id(x_values)
    axarr[2].plot(x_values, y_values)
    canvas.show()


def graphWeather(lat, long, startDate, endDate):

    dates=[]
    data = backend.getAllWeather(lat, long, dates)
    maxs = []
    mins = []
    precis = []
    for i in data:
        maxs.append(i[1])
        mins.append(i[0])
        precis.append(i[2])
    graphPreci(precis)
    graphTemp(maxs)


def graphTemp(maxi, mini):
    maxs = array(maxi)
    mins = array(mini)
    avg = (maxs + mins) / 2
    axarr[0].plot(maxs)
    axarr[0].plot(mins)
    axarr[0].plot(avg)


def graphPreci(precip):
    axarr[1].plot(precip)


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
        graphStocks(startday, endday)
        graphWeather(loc.latitude, loc.longitude,)


root = Tk()
use('TkAgg')
root.wm_title("Embedding in TK")

x = array([1, 4, 5, 7, 6, 5, 76])
y = array([45, 2, 12, 67, 97, 46, 2])

x = array([])
y = array([])
f, axarr = subplots(4)
axarr[0].plot(x, y)
axarr[0].set_title('Weather')
axarr[3].scatter(x, y)
axarr[3].set_title('Happiness')
axarr[1].scatter(x, y)
axarr[1].set_title('Precipitation')
axarr[2].plot(x, y ** 2)
axarr[2].set_title('Stock Exchange')
canvas = FigureCanvasTkAgg(f, master=root)
f.tight_layout()
canvas.show()

canvas.get_tk_widget().pack(side=LEFT, expand=1)

# toolbar = NavigationToolbar2TkAgg(canvas, root)
# toolbar.update()
canvas._tkcanvas.pack(side=LEFT, expand=1)

controlP = Frame(root)
controlP.pack()
Label(controlP, text="Enter Twitter Handle", anchor=NW).grid(row=1, column=1)
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


button = Button(master=root, text='Quit', command=_quit)
button.pack(side=BOTTOM)

root.protocol("WM_DELETE_WINDOW", _quit)
root.mainloop()
