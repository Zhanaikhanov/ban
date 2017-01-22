import random
import tkinter
#constants
B_GROUND = "black"
WIDTH = 640
HEIGHT = 480
TITLE = "TANKS! created by:beka"
SPEEDX = 1
SPEEDY = 0
DELAY = 5
colors=['#157F1F','#A0EADE','#E06C9F','#00A5CF','red']
COUNT=5
#constants

#class
class tanks():
    def __init__(self, x, y, dx=SPEEDX, dy = SPEEDY, color = "red"):
        self.dx = dx
        self.dy = dy
        self.x = x
        self.y = y
        self.color = color
        self.tankss=1
  
 
    def draw(self):

        self.tankss = canvas.create_rectangle(self.x, self.y, self.x+40, self.y+40, fill=self.color, outline=self.color)

    def hide(self):
        
        canvas.delete(self.tankss)
        
    def move(self):
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()
        self.wall()
                            
    def turn_left(self):
        if self.dx<0:
            self.dx = -self.dx
    
    def turn_right(self):
        if self.dx>0:
            self.dx = -self.dx
    
    def wall(self):
        if self.x <= 0 or self.x >=WIDTH-40 :
            self.dx = -self.dx
        if self.y <= 0 or self.y >=HEIGHT-40 :
            self.dy = -self.dy 
class bullets():
    def __init__(self, x, y, dx, dy, l, color='blue'):
        self.x=x+7.5
        self.y=y-7.5
        self.dx=dx
        self.dy=dy
        self.color=color
        self.live=l
        self.fired=0
        self.tankss =1
    def draw(self):
        self.tankss = canvas.create_oval(self.x, self.y, self.x+15, self.y+15, fill=self.color, outline=self.color)
    
    def hide(self):
        canvas.delete(self.tankss)
    def move(self):
        if self.live == 1:
            self.hide()
            self.y += self.dy
            self.draw()
        if self.y+self.dy <=0:
            self.live=1
            self.hide()        
            self.fired=0

class walls():
    def __init__(self, x, y, speed = 1, color= "black"):
        self.x=x
        self.y=y
        self.speed=speed
        self.color=color
        self.tankss = 0
    def draw(self):
        self.tankss = canvas.create_rectangle(self.x, self.y, self.x+30, self.y+5,fill=self.color, outline="black")
    def hide(self):
        canvas.delete(self.tankss)
    def move(self):
        self.hide()
        self.y += self.speed
        self.draw()
        if (self.y + self.speed) >= 640:
            self.hide()
            self.y = 0
            self.x = random.choice(range(0, 450))
            self.draw()
        if self.contact() is True:
            self.hide()
            self.y = 0
            self.x = random.choice(range(0, 450))
            self.draw()
            bullet.live=0
            bullet.fired=0
            bullet.x = -50
            bullet.hide()        


    def contact(self):
        print(1)
        if bullet.x + 15 >= self.x and bullet.x + 15 <=self.x+30 or bullet.x <= self.x+30 and bullet.x + 15 >=self.x+30:   
            if bullet.y+bullet.dy <= self.y+5 and bullet.y+bullet.dy+15 >= self.y+5 :
                return True
#class

#functions
def pressbutton(event):
    if event.num == 3:
        tank.turn_left()
        print("3")
    elif event.num == 2 and bullet.fired==0:
        fire()
    elif event.num == 1:
        print("1")
        tank.turn_right()

def fire():
    bullet.x = tank.x
    bullet.y = tank.y
    bullet.dx = 0
    bullet.dy = -4
    bullet.live=1
    bullet.fired=1


def main():
    tank.move()
    bullet.move()
    for i in lst:
        i.move()
    root.after(DELAY, main)
#functions

root = tkinter.Tk()
root.title(TITLE)
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=B_GROUND)
canvas.pack()
canvas.bind("<Button-1>", pressbutton)
canvas.bind("<Button-2>", pressbutton)
canvas.bind("<Button-3>", pressbutton)
lst = []
for counter in range(0,10):
    y = random.choice(range(-600, 0))
    x = random.choice(range(0, 450))
    color = random.choice(colors)
    new_wall = walls(x,y,1,color)
    lst.append(new_wall)
print(len(lst))
for wall_w in lst:
    wall_w.draw()

tank = tanks(200, 400)
bullet = bullets(0, 0, 0, 0, 0, "blue")

main()
root.mainloop()