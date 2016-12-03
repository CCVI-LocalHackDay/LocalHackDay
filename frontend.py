from tkinter import *
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import subplots
from numpy import *
from geopy.geocoders import Nominatim
import backend


def graphTweets(handle):
    dataSetTweetValue = (backend.getTweetValues(handle))
    print(dataSetTweetValue)
    x = []
    y = []
    keys = []
    for i in dataSetTweetValue:
        keys.append(i)

    keys = sort(keys)
    print(keys)
    for i in keys:
        y.append(dataSetTweetValue[i])
    axarr[0].plot(y)
    print(y)
    canvas.show()

# def graphStocks

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
        graphTweets(tweetHandle)


# Send to Advaity

root = Tk()
use('TkAgg')
root.wm_title("Embedding in TK")

x = array([1, 4, 5, 7, 6, 5, 76])
y = array([45, 2, 12, 67, 97, 46, 2])

x = array([])
y = array([])
f, axarr = subplots(3)
axarr[0].plot(x, y)
axarr[0].set_title('Weather')
axarr[2].scatter(x, y)
axarr[2].set_title('Happiness')
axarr[1].plot(x, y ** 2)
axarr[1].set_title('Stock Exchange')
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
twitterHandleEntry.insert(0,"realdonaldtrump")
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
