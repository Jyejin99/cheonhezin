import turtle
t=turtle.Turtle()
t.shape('turtle')
t.speed(3)
#사각형
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

#삼각형
t.penup()
t.goto(-100,100)
t.pendown()
t.left(30)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)

#육각형
t.penup()
t.goto(-300,100)
t.left(30)
t.pendown()
t.right(90)
t.forward(70)
t.right(60)
t.forward(70)
t.right(60)
t.forward(70)
t.right(60)
t.forward(70)
t.right(60)
t.forward(70)
t.right(60)
t.forward(70)

#별모양
t.penup()
t.goto(200,0)
t.left(30)
t.pendown()
t.right(30)
t.forward(150)
t.right(144)
t.forward(150)
t.right(144)
t.forward(150)
t.right(144)
t.forward(150)
t.right(144)
t.forward(150)
t.right(30)

#올림픽
t.penup()
t.goto(0,-100)
t.pensize(5)
t.color('red')
t.pendown()
t.circle(50)
t.penup()
t.goto(-100,-100)
t.color('black')
t.pendown()
t.circle(50)
t.penup()
t.goto(-200,-100)
t.color('blue')
t.pendown()
t.circle(50)
t.penup()
t.goto(-150,-150)
t.color('yellow')
t.pendown()
t.circle(50)
t.penup()
t.goto(-50,-150)
t.color('green')
t.pendown()
t.circle(50)

#꽃모양
t.penup()
t.goto(200,-100)
t.color('pink')
t.pendown()
for i in range(5):
    t.circle(50)
    t.right(72)
t.color('green')
for i in range(5):
    t.circle(20)
    t.right(72)
    



