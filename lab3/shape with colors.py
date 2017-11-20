import turtle
turtle.speed(0)
turtle.bgcolor("black")
for i in range(500):
    turtle.color("green")
    turtle.forward(300)
    turtle.color("white")
    turtle.right(45)
    turtle.forward(100)
    turtle.color("red")
    turtle.right(90)
    turtle.forward(80)
    turtle.color("green")
    turtle.goto(0,0)
    turtle.right(64)

