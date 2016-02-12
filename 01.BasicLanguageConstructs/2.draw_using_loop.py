import turtle

turtle.speed("fastest")
turtle.color("green")

length = input("Enter length: ")
angle = input("Enter angle: ")

while True:
    turtle.left(int(length))
    turtle.forward(int(angle))