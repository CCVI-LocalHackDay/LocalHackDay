from tkinter import *
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import subplots
from numpy import *
from geopy.geocoders import Nominatim


def getHandleLocation():
    tweetHandle = twitterHandle.get()
    if tweetHandle != "":
        geoL = Nominatim()
        loc = geoL.geocode(location.get())
        if loc is None:
            location.delete(0,END)
            twitterHandle.config(bg="white")
            location.config(bg="red")
        else:
            print(loc)
            print(tweetHandle, loc.latitude, loc.longitude)
    else:
        twitterHandle.config(bg="red")
        location.config(bg="white")
        twitterHandle.delete(0,END)

    location.config(bg="white")
    twitterHandle.config(bg="white")


#   Send to Advaity

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
twitterHandle = Entry(controlP, exportselection=0)
twitterHandle.grid(row=1, column=2)
Label(controlP, text="Enter Location").grid(row=2, column=1)
location = Entry(controlP, exportselection=0)
location.grid(row=2, column=2)

sub = Button(controlP, text="Entry", command=getHandleLocation)
sub.grid(row=5, column=1)


def _quit():
    root.quit()  # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent


button = Button(master=root, text='Quit', command=_quit)
button.pack(side=BOTTOM)

root.mainloop()
