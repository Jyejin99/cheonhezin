import turtle
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.shape("circle")
t2.shape("turtle")

t2.color("green")

t1.penup()
t2.penup()
t1.goto(-100, 0)
t1.write("왼쪽")
t1.goto(0,0)
t1.write("중앙")
t1.goto(100,0)
t1.write("오른쪽")
t1.goto(0,-100)
t1.pendown()


# 숫자를 입력하는 창이 뜬다
s=turtle.textinput("축구 게임","공을 찰 방향을 선택해주세요: ")

if s=="왼쪽":
    t1.goto(-100, 0)
elif s=="중앙":
    t1.goto(0,0)
else:
    t1.goto(100,0)
    
import random
lst = ["왼쪽","중앙","오른쪽"]
com_choice = random.choice(lst)
if com_choice=="왼쪽":
    t2.goto(-100, 0)
elif com_choice=="중앙":
    t2.goto(0,0)
else:
    t2.goto(100,0)
    
if s==com_choice:
    print("당신은 패배했습니다.")
else:
    print("당신은 승리했습니다.")


turtle.done() # 일시정지
