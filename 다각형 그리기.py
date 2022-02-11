import turtle as t       #turtle 라이브러리를 t로 정의
import random as rd

colors=['red','green','blue','orange']
n=int(t.textinput("","몇각형?"))
t.speed(0)
for i in range(100):
    t.pencolor(colors[rd.randrange(4)])
    t.fd(i)
    t.lt(360/n)
t.done()
