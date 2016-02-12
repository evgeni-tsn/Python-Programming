import turtle

length = input("Enter the side of the square. ")

turtle.speed('slowest')
turtle.color('green')

for x in range(0, 4):
    turtle.forward(int(length))
    turtle.left(90)

turtle.exitonclick()