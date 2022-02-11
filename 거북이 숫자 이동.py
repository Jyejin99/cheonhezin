import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(100, 100)
t.write("거북이가 여기로 오면 양수 입니다.")
t.goto(100,0)
t.write("거북이가 여기로 오면 0 입니다.")
t.goto(100,-100)
t.write("거북이가 여기로 오면 음수 입니다.")

t.goto(0,0)
t.pendown()

# 숫자를 입력하는 창이 뜬다
s=turtle.textinput("거북이 게임","숫자를 입력하세요: ")
n=int(s)

if n>0:
    t.goto(100,100)
    t.color('red')
elif n==0:
    t.goto(100,0)
    t.color('blue')
else:
    t.goto(100,-100)
    t.color('purple')

turtle.done() # 일시정지
