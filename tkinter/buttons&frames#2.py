from tkinter import *

root = Tk()     # blank window

topFrame = Frame(root)  # making top frame
topFrame.pack()         # packing frame
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)  #telling where exactly to paCK THE bottom frame (default = top)

### http://effbot.org/tkinterbook/button.htm

button1 = Button(topFrame,text="cccc", fg="red")    # making a button (where to put button, that it says, fg=foreground color)
button2 = Button(topFrame,text="Oyyy", fg="yellow", bg="black") #bg back ground
button3 = Button(topFrame,text="bbbb", fg="blue")
button4 = Button(botFrame,text="Leo Messi", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()


root.mainloop()     # makes sure the window stays open