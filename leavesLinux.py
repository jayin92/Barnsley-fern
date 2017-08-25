import turtle
import random

def f1(point): # 1%
	x = point[0]
	y = point[1]
	x1 = 0
	y1 = 0.16 * y
	return (x1, y1)
def f2(point): # 85%
	x = point[0]
	y = point[1]
	x1 = 0.85 * x + 0.04 * y
	y1 = -0.04 * x + 0.85 * y + 1.6
	return (x1, y1)
def f3(point): # 7%
	x = point[0]
	y = point[1]
	x1 = 0.2 * x - 0.26 * y
	y1 = 0.23 * x + 0.22 * y + 1.6 
	return (x1, y1)
def f4(point): # 7%
	x = point[0]
	y = point[1]
	x1 = -0.15 * x + 0.28 * y
	y1 = 0.26 * x  + 0.24 * y + 0.44
	return (x1, y1)

def drawdot(point):
	turtle.penup()
	turtle.goto((point[0] * 75), (point[1] * 75)-250)
	turtle.pendown()
	turtle.dot(1, 'green')

choices = []
choices.append(1)
for i in range(85):
	choices.append(2)
for i in range(7):
	choices.append(3)
for i in range(7):
	choices.append(4)

random.seed()

turtle.speed(0)
turtle.delay(0)
turtle.hideturtle()
tracepoint = (0, -100)
turtle.resizemode("auto")
i = 1
drawdot(tracepoint)
while True:
	print(i)
	function = random.choice(choices)
	print(function)
	if function == 1:
		tracepoint = f1(tracepoint)
		drawdot(tracepoint)
	elif function == 2:
		tracepoint = f2(tracepoint)
		drawdot(tracepoint)
	elif function == 3:
		tracepoint = f3(tracepoint)
		drawdot(tracepoint)
	elif function == 4:
		tracepoint = f4(tracepoint)
		drawdot(tracepoint)
	print(tracepoint)
	i += 1
