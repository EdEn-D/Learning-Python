from tkinter import *
import time

tk = Tk()     # blank window

canvas = Canvas(tk, width=2200, height=500)
tk.title("Balls")
canvas.pack()

def base():
    canvas.create_line(50,400,2050,400)# number line
    for i in range(101):
        canvas.create_line(50+(i*20), 400, 50+(i*20), 390) # number ticks
        canvas.create_text(50+(i*20), 410, fill="darkblue", font="Times 8 italic bold", text=i) # the actual numbers
        #canvas.create_oval(40+(i*20), 390, 60+(i*20), 370, fill="red")# balls test
base()
timer = 0
i=0
ballsAmount = 11
class Ball:
    def __init__(self, start, color, direction):
        self.shape = canvas.create_oval((start*20) + 40, 390,(start*20) + 60, 370, fill=color)
        self.x = 20*direction
        self.y = 0

    def move(self):
        canvas.move(self.shape, self.x, self.y)
        self.pos = canvas.coords(self.shape)    # pos = [left, top, right, bottom]
        self.numPos = (self.pos[0]-40)/20
        if self.numPos == 0 or self.numPos == 100:
            self.x = -self.x
        #print(i)
        #print(self.pos)

    def get_pos(self):
        return canvas.coords(self.shape)

    def dirChange(self):
        self.x = -self.x
        #print('xxxxxxxxxxx')

#canvas.create_oval(40, 390, 60, 370, fill="black") # ball sample at 0
#50=0, 70=1, 90=2

colors = ['red','green','orange','blue','yellow','cyan','magenta',
          'turquoise','grey','gold','pink']
startPos = [6,14,24,38,44,50,54,64,74,82,88]
direction = [-1,1,-1,-1,1,-1,-1,1,-1,1,1]
balls = []

for i in range(ballsAmount):
    balls.append(Ball(startPos[i],colors[i],direction[i]))

z=0

for c in range(100):
    timer += 1
    #i=0
    for ball in balls:
        ball.move()
        #print(i)
        #print(ball.pos)
        #print(ball.numPos)
        #print(ball.find_overlapping(ball.pos[0], ball.pos[1], ball.pos[2], ball.pos[3]))
        #i += 1
    for j in range(ballsAmount-1):
        k = j + 1
        #print(balls[j].numPos + 0.2222)
        #print(balls[k].numPos + 0.3333)
        if balls[j].numPos == balls[k].numPos:
            balls[j].dirChange()
            balls[k].dirChange()
            #print("shit")
    print(timer)
    tk.update()
    time.sleep(0.21)


tk.mainloop()     # makes sure the window stays open