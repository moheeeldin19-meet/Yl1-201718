import math
import turtle
import random
import time
from ball import Ball
turtle.tracer(1,0)
BALLS=[]
colors=["blue","red","yellow","magenta","orange","green","gray","pink","purple","white","GOLD",]

turtle.bgcolor("black")
SIZE_X= 1000
SIZE_Y= 500

turtle.setup(SIZE_X+50, SIZE_Y+50)

border = turtle.clone()
border.penup()
border.color("white")
border.goto(SIZE_X/2,-SIZE_Y/2)
border.pendown()
border.goto(SIZE_X/2,SIZE_Y/2)
border.goto(-SIZE_X/2,SIZE_Y/2)
border.goto(-SIZE_X/2,-SIZE_Y/2)
border.goto(SIZE_X/2,-SIZE_Y/2)
border.hideturtle()
 
Number_of_balls=30
BLOCKS=[]
screen_width=900/2
screen_height=300/2
MINIMUM_DX=-2
MAXIMUM_DX=2
MINIMUM_DY=-2
MAXIMUM_DY=2
circle=Ball(-475,-200,0,0,10,"white")
win=Ball(0,198,0,0,50,"magenta")
BLOCKS.append(circle)
for i in range(Number_of_balls+2):
    global x,y
    x=random.randint(-screen_width,screen_width)
    y=random.randint(-screen_height,screen_height)
    dx=random.randint(MINIMUM_DX,MAXIMUM_DX)
    dy=random.randint(MINIMUM_DY,MAXIMUM_DY)
    while dx==0 and dy==0:
        dx=random.randint(MINIMUM_DX,MAXIMUM_DX)
        dy=random.randint(MINIMUM_DY,MAXIMUM_DY)
    color=(random.random(), random.random(), random.random())
    block=Ball(x,y,dx,dy,8,color)
    BLOCKS.append(block)
##for i in range(Number_of_balls):
##    global a,s
##    a=a+55
##    s=s
##    dx=random.randint(MINIMUM_DX,MAXIMUM_DX)
##    dy=random.randint(MINIMUM_DY,MAXIMUM_DY)
##    color=(random.random(), random.random(), random.random())
##    block=Ball(a,s,-7,2,8,color)
##    BLOCKS.append(block)
##for i in range(Number_of_balls+3):
##    global d,f
##    d=d+47
##    f=f
##    dx=random.randint(MINIMUM_DX,MAXIMUM_DX)
##    dy=random.randint(MINIMUM_DY,MAXIMUM_DY)
##    color=(random.random(), random.random(), random.random())
##    block=Ball(d,f,5,-1,8,color)
##    BLOCKS.append(block)
##for i in range(Number_of_balls+2):
##    global r,t
##    r=r+50
##    t=t
##    dx=random.randint(MINIMUM_DX,MAXIMUM_DX)
##    dy=random.randint(MINIMUM_DY,MAXIMUM_DY)
##    color=(random.random(), random.random(), random.random())
##    block=Ball(r,t,3,0,8,color)
##    BLOCKS.append(block)

def move_all_balls():
    for i in BLOCKS:
        i.move(500,250)
##while True:
##    move_all_balls()
turtle.resizemode('user')
turtle.penup()
##def move_all_balls():
##    for i in BLOCKS:
##        i.move(screen_width,screen_height)

UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
TIME_STEP = 100
START_LENGTH = 10
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

original_size = 20
r = original_size/2


##turtle.clone()
##circle.shape("circle")
##circle.color("blue")
##CIRCLE_SIZE = 1
##circle.shapesize(CIRCLE_SIZE, CIRCLE_SIZE , 1)   


direction = UP
UP_EDGE = SIZE_Y/2
DOWN_EDGE = -SIZE_Y/2
LEFT_EDGE = -SIZE_X/2
RIGHT_EDGE = SIZE_X/2

def up():
    global direction
    direction = UP
    print('You pressed the up key!')
    
def down():
    global direction
    direction = DOWN
    print('You pressed the down key!')

def left():
    global direction
    direction = LEFT
    print('You pressed the left key!')

def right():
    global direction
    direction = RIGHT
    print('You pressed the right key!')

new_pos = circle.pos()
new_x_pos = new_pos[0]
new_y_pos = new_pos[1]


##def border_hit():
##    if UP_EDGE - new_y_pos <= circle.r*2/2 or new_y_pos - DOWN_EDGE <= circle.r*2/2 or new_x_pos - LEFT_EDGE <= circle.r*2/2 or RIGHT_EDGE - new_x_pos <= circle.r*2/2:          
##        quit()
def move_circle():
    global score
    if direction == RIGHT:
        circle.dx=2
        circle.dy=0
   
    elif direction == LEFT:
        circle.dx=-2
        circle.dy=0

    elif direction == DOWN:
        circle.dy=-2
        circle.dx=0



    elif direction == UP:
        circle.dy=2
        circle.dx=0

    turtle.onkeypress(up, UP_ARROW)
    turtle.onkeypress(down, DOWN_ARROW) 
    turtle.onkeypress(left, LEFT_ARROW)
    turtle.onkeypress(right, RIGHT_ARROW)

    turtle.listen()




  
def check_collision(ball_1,ball_2):
    distance = math.sqrt(math.pow(ball_1.xcor()-ball_2.xcor(),2)+math.pow(ball_1.ycor()-ball_2.ycor(),2))
    if distance  <= ball_1.r+ball_2.r:
        return True

    else:
        return False
                     
def check_my_ball_collision():
    for ball_b in BLOCKS_SUB:
            if check_collision(circle,ball_b)== True:
                turtle.hideturtle()
                turtle.goto(-200,0)
                turtle.color("white")
                turtle.write("GAME OVER!!! you lost" ,align="left",font=("Arial",24,"normal"))
                quit()
                    
def check_win_ball():
        if check_collision(circle,win)== True:
                turtle.hideturtle()
                turtle.goto(-200,0)
                turtle.color("gold")
                turtle.write("YOU WON!!! congrats" ,align="left",font=("Arial",30,"normal"))
                quit()
##            
##def check_my_ball_collision():
##    for ball_b in BALLS:
##            if check_collision(circleball_b)== True:
##                radius_a=circle.r
##                radius_b=ball_b.r
##                x=random.randint(int(-screen_width) +MAXIMUM_BALL_RADIUS,int(screen_width) - MAXIMUM_BALL_RADIUS)
##                y=random.randint(int(-screen_height)+MAXIMUM_BALL_RADIUS,int(screen_height) - MAXIMUM_BALL_RADIUS)
##                dx=random.randint(MINIMUM_Ball_Dx,MAXIMUM_BALL_Dx)
##                dy=random.randint(MINIMUM_BALL_Dy,MAXIMUM_BALL_Dy)
##                while dx ==0:
##                    dx=random.randint(MINIMUM_Ball_Dx,MAXIMUM_BALL_Dx)
##                while dy ==0:
##                    dy=random.randint(MINIMUM_BALL_Dy,MAXIMUM_BALL_Dy)
##                r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
##                color=(random.random(), random.random(), random.random())
##                if ball_b.r> circle.r:
##                    return False
##                else:
##                     circle.r=radius_a+10
##                     circle.shapesize(r/10)
##                     ball_b.shapesize(r/10)
##                     ball_b.goto(x,y)
##                     ball_b.dx=dx
##                     ball_b.dy=dy
##                     ball_b.color(color)
##    return True
##
BLOCKS_SUB=BLOCKS[1:]

    
while True:
    move_all_balls()
    move_circle()
    check_my_ball_collision()
    check_win_ball()
    circle.border_hit(500,250)

##    turtle.listen()

turtle.getscreen().update()
