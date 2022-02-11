import turtle
import time
import random as rd

t=turtle.Turtle()
t.penup()
t.speed(0)
t.right(90)

colors=['red','green','purple','pink']
colors2=['orange','yellow','blue','brown']
for i in range(100):
    t.goto(rd.randrange(-200,200),rd.randrange(-200,200))
    t.pendown()
    t.begin_fill()
    t.color(colors[rd.randrange(4)])
    for i in range(5):
        t.forward(100)
        t.right(144)
    t.end_fill()
    t.penup()

    t.pendown()
    t.begin_fill()
    t.color(colors[rd.randrange(4)])
    t.circle(25,180)
    t.circle(-25,180)
    t.left(180)
    t.circle(50,180)
    t.end_fill()

    t.begin_fill()
    t.color(colors2[rd.randrange(4)])
    t.circle(25,180)
    t.circle(-25,180)
    t.circle(-50,180)
    t.end_fill()
    t.penup()
