import turtle
t=turtle.Turtle()

s=turtle.textinput("","몇 각형을 그리시겠습니까?")
n=int(s)

for i in range(n):
    t.forward(100)
    t.left(360/n)

t.done()

