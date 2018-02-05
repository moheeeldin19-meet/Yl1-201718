from turtle import *

class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.shape("circle")
        self.pu()
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r=r
        self.shapesize(r/10)
        self.color(color)

    def move(self,screen_width,screen_height):       
        self_current_x=self.xcor()
        new_x=self_current_x+self.dx

        self_current_y=self.ycor()
        new_y=self_current_y+self.dy

        right_side_ball= new_x + self.r
        left_side_ball=new_x-self.r
        down_side_ball=new_y-self.r
        up_side_ball=new_y+self.r

        self.goto(new_x,new_y)

        if right_side_ball>=screen_width:
           self.dx=-self.dx
           self.clear()
        if left_side_ball<= -screen_width:
            self.dx=-self.dx
            self.clear()
        if down_side_ball<=-screen_height:
            self.dy=-self.dy
            self.clear()
        if up_side_ball >= screen_height:
            self.dy=-self.dy
            self.clear()
 
