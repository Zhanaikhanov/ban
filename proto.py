import random
import tkinter
#constants
B_GROUND = "black"
WIDTH = 640
HEIGHT = 480
TITLE = "TANKS! created by:beka"
SPEEDX = 2
SPEEDY = 0
DELAY = 10
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

        self.tankss = canvas.create_rectangle(self.x, self.y, self.x+80, self.y+5, fill=self.color, outline=self.color)

    def hide(self):
        
        canvas.delete(self.tankss)
        
    def move(self):
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()
        self.wall()
        self.contact()
                            
    def turn_left(self):
        if self.dx<0:
            self.dx = -self.dx
    
    def turn_right(self):
        if self.dx>0:
            self.dx = -self.dx
    
    def wall(self):
        if self.x <= 0 or self.x >=WIDTH-80 :
            self.dx = -self.dx
        if self.y <= 0 or self.y >=HEIGHT-5 :
            self.dy = -self.dy 
    def contact(self):
        if (bullet.y+bullet.dy >= self.y and bullet.y+bullet.dy<=self.y+5) or (bullet.y+bullet.dy+15 >= self.y and bullet.y+bullet.dy+15<=self.y+5):
            if (bullet.x+15>=self.x and bullet.x<=self.x) or (bullet.x+15<=self.x+80 and bullet.x>=self.x) or (bullet.x+15>=self.x+80 and bullet.x<=self.x+80): 
                bullet.dy = -bullet.dy   
        elif (bullet.x+bullet.dx +15>=self.x and bullet.x+bullet.dx<=self.x) or (bullet.x+bullet.dx+15>=self.x+80 and bullet.x+bullet.dx<=self.x+80):
            if (bullet.y+bullet.dy >= self.y and bullet.y+bullet.dy<=self.y+5) or (bullet.y+bullet.dy+15 >= self.y and bullet.y+bullet.dy+15<=self.y+5):            
                bullet.dx = -bullet.dx 
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
            self.x += self.dx
            self.draw()
        if self.y+self.dy <=0:
            self.live=1
            self.y = HEIGHT
            self.hide()        
            self.fired=0
        self.wall()
    def wall(self):
        if self.x <= 0 or self.x >=WIDTH-15 :
            self.dx = -self.dx
        if self.y <= 0 or self.y >=HEIGHT-15 :
            self.dy = -self.dy   

class walls():
    def __init__(self, x, y, color= "black"):
        self.x=x
        self.y=y
        self.color=color
        self.tankss = 0
    def draw(self):
        self.tankss = canvas.create_rectangle(self.x, self.y, self.x+30, self.y+5,fill=self.color, outline="black")
    def hide(self):
        canvas.delete(self.tankss)

    def contact(self):
        if bullet.y + bullet.dy >= HEIGHT:  
            self.hide()
            self.x = -100
            bullet.live=1
            bullet.hide()
            bullet.y = 0        
            bullet.fired=0
        if bullet.x + 15 >= self.x and bullet.x + 15 <=self.x+30 or bullet.x <= self.x+30 and bullet.x + 15 >=self.x+30:   
            if bullet.y+bullet.dy <= self.y and bullet.y+bullet.dy+15 >= self.y+5 :
                self.hide()
                self.x = -100
                bullet.live=1
                bullet.fired=1
                bullet.dy = -bullet.dy
                

#class

#functions
def pressbutton(event):
    if event.num == 3:
        tank.turn_left()
    elif event.num == 2 and bullet.fired==0:
        fire()
    elif event.num == 1:
        tank.turn_right()

def fire():
    bullet.x = tank.x
    bullet.y = tank.y
    bullet.dx = tank.dx-1
    bullet.dy = -1
    bullet.live=1
    bullet.fired=1


def main():
    tank.move()
    bullet.move()
    for i in lst:
        i.contact()
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
    y = random.choice(range(0, 300))
    x = random.choice(range(0, 450))
    color = random.choice(colors)
    new_wall = walls(x,y,color)
    lst.append(new_wall)
    new_wall.draw()
print(len(lst))
#for wall_w in lst:
#    wall_w.draw()

tank = tanks(200, 400)
bullet = bullets(0, 0, 0, 0, 0, "blue")

main()
root.mainloop()