import turtle

t=turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

square(100)
square(200)
square(300)
turtle.done()
