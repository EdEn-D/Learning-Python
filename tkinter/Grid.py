from tkinter import *

root = Tk()     # blank window

label1 = Label(root, text="Name")
label2 = Label(root, text="Password")
entry1 = Entry(root)    # requests input
entry2 = Entry(root)
# organizes the label according to the grid (column is 0 by default)
label1.grid(sticky=E,row=0)      # sticky tells where to stick the label based on N, S, E, W (compass)
label2.grid(row=1,sticky=E)
entry1.grid(row =0, column=1)
entry2.grid(row =1, column=1)

# checkbox

cBox = Checkbutton(root, text="Keep me logged in")
cBox.grid(columnspan=2)

root.mainloop()     # makes sure the window stays open