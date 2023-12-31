import turtle


screen = turtle.Screen()
screen.title("Netherlands Flag")
screen.setup(width=600, height=400)


turtle.penup()
turtle.goto(-300, 100)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()


turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-300, -100)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()


turtle.hideturtle()


turtle.done()