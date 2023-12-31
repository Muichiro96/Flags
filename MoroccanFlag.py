import turtle
from asyncio import sleep

screen = turtle.Screen()
screen.title("Moroccan  Flag")
screen.setup(width=600, height=600)
turtle.up()
turtle.goto(-300,100)
turtle.down()
turtle.color("red")
turtle.begin_fill()
turtle.forward(600)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(300)
turtle.end_fill();
turtle.up()
turtle.goto(-20,-5)

turtle.setheading(0)
turtle.heading()
turtle.down()
turtle.color("green")
turtle.right(75)
turtle.forward(100)
turtle.dot()
for i in range(4):
    turtle.right(144)
    turtle.forward(100)
    turtle.dot()

turtle.right(69)
turtle.done()