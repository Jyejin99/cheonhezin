# 주급 계산 프로그램

def weeklyPay(rate,hour):
    if(hour>48):
        money=rate*48+1.5*rate*(hour-48)
    else:
        money=rate*hour
    return money

r=int(input("시급을 입력하시오: "))
h=int(input("근무시간을  입력하시오: "))
print("주급은"+str(weeklyPay(rate=r,hour=h)))
