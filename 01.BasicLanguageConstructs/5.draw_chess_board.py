import turtle
import random

side = 30
randomColor = ['green', 'red', 'blue', 'orange', 'grey', 'black', 'lime', 'brown', 'pink', 'purple']
turtle.speed('fastest')
for i in range(8):
    if i % 2 == 0:
        for i in range(8):
            # turtle.color(random.choice(randomColor))
            if i % 2 == 0:
                turtle.begin_fill()
            for i in range(4):
                turtle.forward(side)
                turtle.left(90)
            turtle.end_fill()
            turtle.forward(side)
        turtle.left(90)
        turtle.forward(side * 2)
        turtle.left(90)
    else:
        for i in range(8):
            # turtle.color(random.choice(randomColor))
            if i % 2 == 0:
                turtle.begin_fill()
            for i in range(4):
                turtle.forward(side)
                turtle.left(90)
            turtle.end_fill()
            turtle.forward(side)
        turtle.right(180)
turtle.exitonclick()
