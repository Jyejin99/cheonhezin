import turtle   
import random as rd

t=turtle.Turtle()
t.speed(0)

def triangle(n):
    for i in range(1,n+1):
        t.penup()
        t.goto(rd.randrange(-200,200),rd.randrange(-200,200))
        t.pendown()
        for z in range(3):
            t.fd(100)
            t.left(120)

n=int(turtle.textinput("","정수를 입력해주세요: "))
print(triangle(n))
