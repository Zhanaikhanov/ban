import random
import tkinter
#constants
B_GROUND = "black"
WIDTH = 640
HEIGHT = 480
TITLE = "TANKS! created by:beka"
SPEEDX = 1
SPEEDY = 0
DELAY = 10
colors=['#157F1F','#A0EADE','#E06C9F','#00A5CF','red']
COUNT=5
gt=0
you=9
unu = 0
tui = 0
#constants

#class
class tanks():
    def __init__(self, x, y, dx=SPEEDX, dy = SPEEDY, color = "red"):
        self.dx = dx
        self.dy = dy
        self.x = x
        self.y = y
        self.color = color
        self.scores=0
        self.tankss=1
        self.tankss2 =2 
 
    def draw(self):

        self.tankss = canvas.create_rectangle(self.x, self.y, self.x+30, self.y+40, fill=self.color, outline=self.color)

    def hide(self):
        self.tankss2 = canvas.create_rectangle(self.x, self.y, self.x+30, self.y+40, fill=B_GROUND, outline=B_GROUND)
        canvas.delete(self.tankss)
        canvas.delete(self.tankss2)

    def move(self):
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()
        self.wall()
        self.score()
        global gt
        while gt <= COUNT:
            x = random.choice(range(10, 600))
            y = random.choice(range(0,480))
            color = random.choice(colors)
            new_wall = walls(x, y, 1, color)
            lst1.append(new_wall)
            new_wall.draw()
            print(1)
            gt += 1
        gt += 2
                            
    def turn_left(self):
        if self.dx<0:
            self.dx = -self.dx
    
    def turn_right(self):
        if self.dx>0:
            self.dx = -self.dx
    
    def wall(self):
        if self.x <= 0 or self.x >=WIDTH-30 :
            self.dx = -self.dx
        if self.y <= 0 or self.y >=HEIGHT-40 :
            self.dy = -self.dy 
    def score(self):
        canvas.create_rectangle(WIDTH/2-15 , 30, WIDTH/2+15, 60, fill='white',outline="black")
        tee = str(self.scores)
        canvas.create_text(WIDTH/2 , 50 , text=tee, font='Arial 20')

class bullets():
    def __init__(self, x, y, dx, dy, l, color='blue'):
        self.x=x+7.5
        self.y=y-7.5
        self.dx=dx
        self.dy=dy
        self.color=color
        self.live=l
        self.fired=0
        self.contact = 0
        self.tankss= 1
        self.tankss2 =2
        self.started = 0
    def draw(self):
        
        self.tankss = canvas.create_oval(self.x, self.y, self.x+15, self.y+15, fill=self.color, outline=self.color)
    
    def hide(self):
        canvas.delete(self.tankss)
    def move(self):
        if self.started == 0:
            self.draw()
            self.started = 1
        if self.live == 1:
            self.hide()
            self.x += self.dx
            self.y += self.dy
            self.draw()
        if self.x+self.dx+15 >= WIDTH or self.x+self.dx <=0 :
            self.live=1
            self.hide()
            self.fired=0
        if self.y+self.dy+15 >= HEIGHT or self.y+self.dy <=0 :
            self.live=1
            self.hide()        
            self.fired=0
        if self.contact is 1:
            self.live=0
            self.hide()
            self.fired=0
            self.contact = 0
             
class walls():
    def __init__(self, x, y, speed = 1, color= "black"):
        self.x=x
        self.y=y
        self.speed=speed
        self.color=color
        self.tankss2 = 2 
        self.tankss = 0
        self.started = 0
    def draw(self):
        self.tankss = canvas.create_rectangle(self.x, self.y, self.x+30, self.y+5,fill=self.color, outline="black")
    def hide(self):
        self.tankss = canvas.create_rectangle( self.x, self.y, self.x+30, self.y+5,fill=B_GROUND, outline=B_GROUND)
        canvas.delete(self.tankss)
        #canvas.delete(self.tankss2)
    def move(self):
        if self.started == 0:
            self.draw()
            self.started = 1
        self.y += self.speed
        if self.contact():
            self.teleport_to_zero()
            bullet.contact = 1
            tank.scores += 1
            print(76)
        if self.y >= 500:
            self.teleport_to_zero()
        if self.is_collision():
            tank.dx = -tank.dx
    def teleport_to_zero(self):
        self.hide()
        self.y = 0
        self.x = random.choice(range(0,450))
        self.draw()
    def contact(self):
        if (bullet.x+15>=self.x) and (bullet.x<=self.x+30) and (bullet.y+bullet.dy+15>=self.y) and (bullet.y+bullet.dy<=self.y+5):
            return True
        else:
            return False
    def is_collision(self):
        if (tank.x+tank.dx+30>=self.x) and (tank.x+tank.dx<=self.x+30) and (tank.y+tank.dy+40>=self.y) and (tank.y+tank.dy<=self.y+5):
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

def wall_g():
    lst=[]
    x = random.choice(range(10, 640))
    y = 0
    color = random.choice(colors)
    new_wall = walls(x, y, 1, color)
    lst.append(new_wall)
    return lst


def main():
    tank.move()
    bullet.move()
   
    root.after(DELAY, main)
#functions

root = tkinter.Tk()
root.title(TITLE)
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=B_GROUND)
canvas.pack()
canvas.bind("<Button-1>", pressbutton)
canvas.bind("<Button-2>", pressbutton)
canvas.bind("<Button-3>", pressbutton)  
tank = tanks(200, 400)
bullet = bullets(0, 0, 0, 0, 0, "blue")
lst1 = []
# wall_g()
main()
root.mainloop()