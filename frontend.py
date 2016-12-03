from tkinter import *
from matplotlib import *
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.pyplot import subplots
from numpy import *
from matplotlib.figure import Figure

root = Tk()
use('TkAgg')
root.wm_title("Embedding in TK")

x =  array([1, 4, 5, 7, 6, 5, 76])
y = array([45, 2, 12, 67, 97, 46, 2])
f, axarr = subplots(3)
axarr[0].plot(x, y)
axarr[0].set_title('Weather')
axarr[2].scatter(x, y)
axarr[2].set_title('Happiness')
axarr[1].plot(x, y ** 2)
axarr[1].set_title('Stock Exchange')
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()

canvas.get_tk_widget().pack(side=LEFT, expand=1)

# toolbar = NavigationToolbar2TkAgg(canvas, root)
# toolbar.update()
canvas._tkcanvas.pack(side=LEFT, expand=1)

controlP = Frame(root)
controlP.pack()
Label(controlP,text="Enter Twitter Handle",anchor=NW).grid(row=1,column=1)
Entry(controlP).grid(row=2, column=1)

sub = Button(controlP, text="Entry")
sub.pack()



def _quit():
    root.quit()  # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent


button = Button(master=root, text='Quit', command=_quit)
button.pack(side=BOTTOM)

root.mainloop()
