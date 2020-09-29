from tkinter import *
import time
import random

tk = Tk()     # blank window
WIDTH=2200
HEIGHT=600

canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Balls")
canvas.pack()

def base():
    canvas.create_line(50,400,2050,400)# number line
    for i in range(101):
        canvas.create_line(50+(i*20), 400, 50+(i*20), 390) # number ticks
        canvas.create_text(50+(i*20), 410, fill="darkblue", font="Times 8 italic bold", text=i) # the actual numbers
        #canvas.create_oval(40+(i*20), 390, 60+(i*20), 370, fill="red")# balls test
    canvas.create_oval(40, 390, 60, 370, fill="red") # ball sample.

class Ball:
    def __init__(self, color, size):
        self.shape = canvas.create_oval(10, 10, size, size, fill=color)
        self.xspeed = random.randrange(1,10)
        self.yspeed = random.randrange(1,10)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)  # pos = [left, top, right, bottom]
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

newball = Ball("red", 50)
newball2 = Ball("green", 100)
newball3 = Ball("blue", 80)

base()
while True:

    newball.move()
    newball2.move()
    newball3.move()
    tk.update()
    time.sleep(0.01)


tk.mainloop()     # makes sure the window stays open