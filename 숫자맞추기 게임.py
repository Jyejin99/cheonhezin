# 무한 반복문으로 숫자를 맞추는 게임

import random

tries = 0
guess = 0
answer=random.randint(1,100)
print("1부터 100사이의 숫자를 맞추시오")

while True:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries+1
    if guess < answer:
        print("낮음!")
    elif guess > answer:
        print("높음!")
    if tries == 10:
        print("실패하였습니다. 총 시도횟수=", tries)
        break
    elif (guess==answer):
        print("축하합니다! 총 시도횟수=",tries)
        break
