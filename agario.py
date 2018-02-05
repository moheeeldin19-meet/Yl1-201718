##set up
import turtle,random,time,math
from ball import Ball
turtle.tracer(0)
turtle.hideturtle()
Running= True
sleep=0.1
screen_width=turtle.getcanvas().winfo_width()/2
screen_height= turtle.getcanvas().winfo_height()/2


       

##setup pt.2
MY_BALL=Ball(0,0,200,200,200,"darkgray")
Number_of_balls=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_Ball_Dx=1
MAXIMUM_BALL_Dx=3
MAXIMUM_BALL_Dy=3
MINIMUM_BALL_Dy=1
BALLS=[]
#just making sure it's an int

##making diffrent balls
for i in range(Number_of_balls):
    x=random.randint(round(-screen_width) + MAXIMUM_BALL_RADIUS,round(screen_width) - MAXIMUM_BALL_RADIUS)
    y=random.randint(round(-screen_height) + MAXIMUM_BALL_RADIUS,round(screen_width) - MAXIMUM_BALL_RADIUS)
    dx=random.randint(MINIMUM_Ball_Dx,MAXIMUM_BALL_Dx)
    dy=random.randint(MINIMUM_BALL_Dy,MAXIMUM_BALL_Dy)
    while dx==0 or dy==0:
        dx=random.randint(MINIMUM_Ball_Dx,MAXIMUM_BALL_Dx)
        dy=random.randint(MINIMUM_BALL_Dy,MAXIMUM_BALL_Dy)
        
    r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color=(random.random(), random.random(), random.random())
    circle=Ball(x,y,dx,dy,r,color)
    BALLS.append(circle)
    
    
    #moving the circles
def move_all_balls():
    for Circle in BALLS:
        Circle.move(screen_width,screen_height)
        
def check_collision(ball1,ball2):
    distance = math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2)+math.pow(ball1.ycor()-ball2.ycor(),2))
    if distance + 10 <= ball1.r+ball2.r:
        return True

    else:
        return False

def check_all_collisions():
     for ball_a in BALLS:
         for ball_b in BALLS:
             if check_collision(ball_a,ball_b) == True:
                 radius_a=ball_a.r
                 radius_b = ball_b.r
                 x=random.randint(round(-screen_width) +MAXIMUM_BALL_RADIUS,round(screen_width) - MAXIMUM_BALL_RADIUS)
                 y=random.randint(round(-screen_height)+MAXIMUM_BALL_RADIUS,round(screen_height) - MAXIMUM_BALL_RADIUS)
                 dx=random.randint(MINIMUM_Ball_Dx,MAXIMUM_BALL_Dx)
                 while dx ==0:
                     dx=random.randint(MINIMUM_Ball_Dx,MAXIMUM_BALL_Dx)
                 dy=random.randint(MINIMUM_BALL_Dy,MAXIMUM_BALL_Dy)
                 while dy ==0:
                     dy=random.randint(MINIMUM_BALL_Dy,MAXIMUM_BALL_Dy)    
                 r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                 color=(random.random(), random.random(), random.random())
                 if ball_a.r> ball_b.r:
                     ball_a.r=ball_a.r + 1
                     ball_a.shapesize(ball_a.r/10)
                     ball_b.goto(x,y)
                     ball_b.dx=dx
                     ball_b.dy=dy
                     ball_b.color(color)
                     ball_b.r = r
                     ball_b.shapesize(r/10)
                 else:
                     ball_b.r=ball_b.r+1
                     ball_b.shapesize(ball_b.r/10)
                     ball_a.goto(x,y)
                     ball_a.dx=dx
                     ball_a.dy=dy
                     ball_a.color(color)
                     ball_a.r = r
                     ball_a.shapesize(r/10)
                     
def check_my_ball_collision():
    for ball_b in BALLS:
            if check_collision(MY_BALL,ball_b)== True:
                radius_a=MY_BALL.r
                radius_b=ball_b.r
                x=random.randint(int(-screen_width) +MAXIMUM_BALL_RADIUS,int(screen_width) - MAXIMUM_BALL_RADIUS)
                y=random.randint(int(-screen_height)+MAXIMUM_BALL_RADIUS,int(screen_height) - MAXIMUM_BALL_RADIUS)
                dx=random.randint(MINIMUM_Ball_Dx,MAXIMUM_BALL_Dx)
                dy=random.randint(MINIMUM_BALL_Dy,MAXIMUM_BALL_Dy)
                while dx ==0:
                    dx=random.randint(MINIMUM_Ball_Dx,MAXIMUM_BALL_Dx)
                while dy ==0:
                    dy=random.randint(MINIMUM_BALL_Dy,MAXIMUM_BALL_Dy)
                r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color=(random.random(), random.random(), random.random())
                if ball_b.r> MY_BALL.r:
                    return False
                else:
                     MY_BALL.r=radius_a+10
                     MY_BALL.shapesize(r/10)
                     ball_b.shapesize(r/10)
                     ball_b.goto(x,y)
                     ball_b.dx=dx
                     ball_b.dy=dy
                     ball_b.color(color)
    return True

def movearound(event):
    x= event.x - round(screen_width)
    y=round(screen_height) -event.y
    MY_BALL.goto(x,y)
turtle.getcanvas().bind("<Motion>", movearound)
#turtle.getscreen().listen()
turtle.listen()

while  Running ==True:
    while  screen_width!=turtle.getcanvas().winfo_width()/2 or screen_height !=turtle.getcanvas().winfo_height()/2:
        screen_width=turtle.getcanvas().winfo_width()/2
        screen_height=turtle.getcanvas().winfo_height()/2
    move_all_balls()
    check_all_collisions()
    check_my_ball_collision()
    if check_my_ball_collision==True:
         Running=False
    turtle.getscreen().update()
    time.sleep(sleep)
##    
check_my_ball_collision()
