# 정삼각형 그리는 함수

import turtle   
import random as rd

n=int(turtle.textinput("","정수를 입력해주세요: "))
for i in range(1,n+1):
    t=turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(rd.randrange(-200,200),rd.randrange(-200,200))
    t.pendown()
    for z in range(3):
        t.fd(100)
        t.left(120)
turtle.done()


