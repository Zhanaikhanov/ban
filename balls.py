import tkinter
import random
WIDTH=480
HEIGHT=640
BG_COLOR='white'
colors=['#157F1F','#A0EADE','#E06C9F','#00A5CF','red']
NUM_OF_BALLS=5
DELAY=10

class Ball():
	"""docstring fos Ball"""
	def __init__(self, x, y, r, color, dx=0, dy=0):
		self.x = x
		self.y = y
		self.r = r
		self.color = color
		self.dx = dx
		self.dy = dy		

	def draw(self):
		canvas.create_oval(self.x - self.r, self.y-self.r, self.x + self.r, self.y+self.r, fill=self.color, outline=self.color)

	def hide(self):
		canvas.create_oval(self.x - self.r, self.y-self.r, self.x + self.r, self.y+self.r, fill=BG_COLOR, outline=BG_COLOR)

	def is_collision(self, ball):
		a = abs(self.x - ball.x + self.dx)
		b = abs(self.y - ball.y + self.dy)
		return (a*a + b*b)**0.5 <= self.r + ball.r

	def move(self):
		if (self.x+self.r+self.dx >= WIDTH or self.x-self.r+self.dx <= 0):
			self.dx= -self.dx
		elif (self.y+self.r+self.dy >= HEIGHT or self.y-self.r+self.dy <= 0):
			self.dy= -self.dy
		for ball in balls:
			if self.is_collision(ball):
				if ball.color != 'red':
					ball.hide()
					balls.remove(ball)
					self.dx = -self.dx
					self.dy = -self.dy
				else:
					self.dx = self.dy = 0
					canvas.create_text(WIDTH/2, HEIGHT/2, text='Game over!', font='Arial 20')


		self.hide()
		self.x += self.dx
		self.y += self.dy
		self.draw()


def mouse_click(event):
	if event.num == 2:
		Balls=Ball(event.x, event.y, 20, 'blue')
		Balls.hide()
	if 'Balls' not in globals():
		global Balls
		if event.num == 1:
			Balls=Ball(event.x, event.y, 20, 'blue', 1, 1)
			Balls.draw()
			Balls.move()
	elif event.num == 3:
		if Balls.dx * Balls.dy < 0:
			Balls.dy = -Balls.dy
		elif Balls.dx * Balls.dy > 0:
			Balls.dx = -Balls.dx		
	elif event.num == 1:
		if Balls.dx * Balls.dy > 0:
			Balls.dy = -Balls.dy
		elif Balls.dx * Balls.dy < 0:
			Balls.dx = -Balls.dx		


def count_bad(list_balls):
	res=0
	for cou in list_balls:
		if cou.color == 'red':
			res += 1
	return res	

def main():
	if 'Balls' in globals() :
		Balls.move()
	root.after(DELAY , main)
	if len(balls) - count == 0:
		canvas.create_text(WIDTH/2 , HEIGHT/2 , text="you won!", font='Arial 20')
		Balls.dx = Balls.dy = 0

def create_list(number):
	lst=[]
	while len(lst) <= number:
		radius1 = random.choice(range(15 , 30) )
		width1 = random.choice(range(radius1 , WIDTH - radius1))
		height1 = random.choice(range(radius1 , HEIGHT - radius1) )
		color1 = random.choice(colors) 
		next_ball = Ball(width1, height1, radius1, color1)
		lst.append(next_ball)
		next_ball.draw()

	radius1 = random.choice(range(15 , 30) )
	height1 = random.choice(range(radius1 , HEIGHT - radius1) )
	color1 = "red" 	
	next_ball = Ball(width1, height1, radius1, color1)
	lst.append(next_ball)
	next_ball.draw()
	
	return lst



root = tkinter.Tk()
root.title("Bektemir's first balls in the python!")
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click)
canvas.bind('<Button-3>', mouse_click)
balls = create_list(NUM_OF_BALLS)
count = count_bad(balls)
print(count)
main()
root.mainloop()
