import turtle
import random

tim = turtle.Turtle()
Colors = ['black','yellow','pink','green','blue','gray','purple','orange', 'lightyellow']
tim.width(2)
for x in range(30):
	rad1 = random.randrange(-300,300)
	rad2 = random.randrange(-300,300)

	tim.penup()
	tim.setpos(rad1,rad2)
	tim.pendown()

	col1 = random.randrange(len(Colors))
	col2 = random.randrange(len(Colors))
	tim.color(Colors[col1],Colors[col2])
	x =  random.randrange(30,90)
	tim.begin_fill()
	tim.circle(x)
	tim.end_fill()

turtle.done()
