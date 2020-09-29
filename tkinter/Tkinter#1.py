from tkinter import *

root = Tk()     # blank window
theLabel = Label(root, text='Test/practice GUI app')  # basic text is called a label in tkinter
theLabel.pack()     # pack it in the root window, no exact location
root.mainloop()     # makes sure the window stays open