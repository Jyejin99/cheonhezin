import turtle
import random as rd

t=turtle.Turtle()
t.speed(0)
turtle.colormode(255)
t.hideturtle()
t.right(90)

def getRGB():
    r=rd.randrange(0,256)
    g=rd.randrange(0,256)
    b=rd.randrange(0,256)
    return r,g,b

def location(x,y):
    x1=rd.randrange(x/2)
    y1=rd.randrange(y/2)
    t.goto(x1,y1)

def triangle(r):    
    for i in range(3):
        t.color(getRGB())
        t.fd(r)
        t.left(120)

triangle(100)
location(100,400)


