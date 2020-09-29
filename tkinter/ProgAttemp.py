from tkinter import *
import time

tk = Tk()     # blank window

canvas = Canvas(tk, width=2200, height=600)
tk.title("Balls")
canvas.pack()

def base():
    canvas.create_line(50,400,2050,400)# number line
    for i in range(101):
        canvas.create_line(50+(i*20), 400, 50+(i*20), 390) # number ticks
        canvas.create_text(50+(i*20), 410, fill="darkblue", font="Times 8 italic bold", text=i) # the actual numbers
        #canvas.create_oval(40+(i*20), 390, 60+(i*20), 370, fill="red")# balls test
base()

class Ball:
    def __init__(self, start, color, direction):
        self.shape = canvas.create_oval((start*20) + 40, 390,(start*20) + 60, 370, fill=color)
        self.x = 20*direction
        self.y = 0

    def move(self):
        canvas.move(self.shape, self.x, self.y)
        pos = canvas.coords(self.shape) # pos = [left, top, right, bottom]
        if pos[2] >= 'another ball' or pos[0] <= 'another ball':
            self.xspeed = -self.xspeed


#canvas.create_oval(40, 390, 60, 370, fill="black") # ball sample.

colors = ['red','green','blue','orange','yellow','cyan','magenta',
          'turquoise','grey','gold','pink']
startPos = [24,52,60,84]
direction = [1,-1,1,-1]
balls = []

for i in range(4):
    balls.append(Ball(startPos[i],colors[i],direction[i]))


while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.5)


tk.mainloop()     # makes sure the window stays open