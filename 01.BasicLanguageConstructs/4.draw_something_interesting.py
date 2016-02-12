import turtle
import random

turtle.speed(1000)
turtle.width(5)

i = 10

randomColor = ['green', 'red', 'blue', 'orange', 'grey', 'aqua', 'lime', 'brown', 'pink', 'purple']

while True:
	turtle.color(random.choice(randomColor))
	turtle.left(i % 23 * 113)
	turtle.forward(50)
	i += 500
