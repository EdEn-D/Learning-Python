from tkinter import *

root = Tk()     # blank window

one = Label(root, text='One', bg='red', fg='yellow')
one.pack()
two = Label(root, text='Two', bg='blue', fg='orange')
two.pack(fill=X)    # button will fill the widget/window as big as the window is
three = Label(root, text='Three', bg='green', fg='purple')
three.pack(side=LEFT, fill = Y)

root.mainloop()     # makes sure the window stays open