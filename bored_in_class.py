import turtle,random
turtle.width(10)
turtle.speed(0)
x=0
colors=["red","blue","cyan","magenta","gold","gray","black","yellow","orange","green"]
while True:
    color=random.choice(colors)
    turtle.color(color)
    x=x+5
    turtle.forward(x)
    turtle.right(172)
