##set up
import turtle,random,time,math
from ball import Ball
turtle.tracer=0
turtle.hideturtle()
Running= True
sleep=0.0077
screen_width=int(turtle.getcanvas().winfo_width()/2)
screen_height= int(turtle.getcanvas().winfo_height()/2)


       

##setup pt.2
MY_BALL=Ball(0,0,1,1,100,"darkgray")
Number_of_balls=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_Ball_Dx=-5
MAXIMUM_BALL_Dx=5
MAXIMUM_BALL_Dy=5
MINIMUM_BALL_Dy=-5
BALLS=[]
p=0
#just making sure it's an int

print(screen_width +MAXIMUM_BALL_RADIUS )
print(screen_width - MAXIMUM_BALL_RADIUS)
##making diffrent balls
for i in range(Number_of_balls):
    x=random.randint(-screen_width +MAXIMUM_BALL_RADIUS,screen_width - MAXIMUM_BALL_RADIUS)
    y=random.randint(-screen_height+MAXIMUM_BALL_RADIUS,screen_width - MAXIMUM_BALL_RADIUS)
    dx=random.randint(MINIMUM_Ball_Dx,MAXIMUM_BALL_Dx)
    dy=random.randint(MINIMUM_BALL_Dy,MAXIMUM_BALL_Dy)
    r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    s_w=random.randint(-screen_width,screen_width)
    s_h=random.randint(-screen_height,screen_height)
    color=(random.random(), random.random(), random.random())
    circle=Ball(x,y,dx,dy,r,color)
    BALLS.append(circle)
    
    
    #moving the circles
def move_all_balls():
    for i in range(len(BALLS)+100):
        w=random.randint(-200,200)
        h=random.randint(-200,200)
        BALLS[0].move(w,h)
        BALLS[1].move(w,h)
        BALLS[2].move(w,h)
        BALLS[3].move(w,h)
        BALLS[4].move(w,h)
        
def check_collision(ball1,ball2):
    if math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2)+math.pow(ball1.ycor()-ball2.ycor(),2))<= ball1.r+ball2.r:
        return(True)

    else:
        return(False)

def check_all_collisions():
     for ball_a in BALLS:
         for ball_b in BALLS:
             if check_collision(ball_a,ball_b) ==True:
                 radius_a=ball_a.r
                 radius_a = ball_b.r
                 x=random.randint(-screen_width +MAXIMUM_BALL_RADIUS,screen_width - MAXIMUM_BALL_RADIUS)
                 y=random.randint(-screen_height+MAXIMUM_BALL_RADIUS,screen_width - MAXIMUM_BALL_RADIUS)
                 dx=random.randint(MINIMUM_Ball_Dx,MAXIMUM_BALL_Dx)
                 if dx ==0:
                     dx=random.randint(MINIMUM_Ball_Dx,MAXIMUM_BALL_Dx)
                 dy=random.randint(MINIMUM_BALL_Dy,MAXIMUM_BALL_Dy)
                 if dy ==0:
                     dy=random.randint(MINIMUM_BALL_Dy,MAXIMUM_BALL_Dy)    
                 r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                 s_w=random.randint(-screen_width,screen_width)
                 s_h=random.randint(-screen_height,screen_height)
                 color=(random.random(), random.random(), random.random())
                 if ball_a.r> ball_b.r:
                     ball_a.r=ball_a.r+ball_b.r
                     ball_b.r=0
                     ball_b=Ball(x,y,dx,dy,r,color)
                     ball_a.shapesize(r/10)
                 if ball_a.r<ball_b.r:
                     ball_a=Ball(x,y,dx,dy,r,color)
                     ball_b.r=ball_b.r+ball_a.r
                     ball_a.shapesize(r/10)
                     ball_b.shapesize(r/10)

def check_my_ball_collision():
    for MY_BALL in BALLS:
        if check_collision(MY_BALL,ball2)== True:
            radius_a=MY_BALL.r
            radius_b=ball_b.r
        
