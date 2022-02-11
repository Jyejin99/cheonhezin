# 섭씨 온도를 화씨 온도로 변환하는 함수

def celsius(x):
    a=(x-32)*5/9
    return a

x=int(input("섭씨온도를 입력해주세요.: "))
print(celsius(x))
