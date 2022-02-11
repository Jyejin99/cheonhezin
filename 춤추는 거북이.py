import turtle as t
import random as rd

t1=t.Turtle()
t2=t.Turtle()
t3=t.Turtle()

t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")

t1.speed(0)
t2.speed(0)
t3.speed(0)

t1.penup()
t2.penup()
t3.penup()

for i in range(100):
    t1.goto(rd.randrange(50,100),rd.randrange(100,150))
    t2.goto(rd.randrange(-150,-100),rd.randrange(-50,0))
    t3.goto(rd.randrange(-150,150),rd.randrange(50,100))
    t1.left(rd.randrange(0,500))
    t2.left(rd.randrange(0,500))
    t3.left(rd.randrange(0,500))

