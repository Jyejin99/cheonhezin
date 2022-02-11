'''
import numpy as np
import matplotlib.pyplot as plt

x = [i for i in range(100)]
y = [i**2 for i in range(100)]
z = [100*np.sin(3.14*i/100) for i in range(100)]

plt.subplot(221)
plt.plot(x,y,x,z)

plt.subplot(222)
plt.plot(x)
plt.subplot(223)
plt.plot(y)
plt.subplot(224)
plt.plot(z)
plt.show()

result = np.corrcoef([x,y,z])
print(result)
'''

# -------------------------------------
'''
import matplotlib.pyplot as plt

#우리나라의 연간 1인당 국민소득을 각각 years, gdp에 저장
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]

#선 그래프를 그린다. x축에는 years값, y축에는 gdp값이 표시된다.
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

#제목을 설정한다.
plt.title("GDP per capita")#1인당 국민소득

#y축에 레이블을 붙인다.
plt.ylabel("dollars")
plt.savefig("gdp_per_caplita.png",dpi=600) #png 이미지로 저장 가능
plt.show()

'''

# ---------------------------------------
import matplotlib.pyplot as plt
# -20에서 20사이의 수를 1의 간격으로 생성
x = [x for x in range(-20,20)]
# 2*x를 원소로 가지는 y1 함수
y1 = [2*t for t in x]
# x**2+5를 원소로 가지는 y2 함수
y2 = [t**2+5 for t in x]
# -x**2-5를 원소로 가지는 y3 함수
y3 = [-t**2-5 for t in x]
# 빨강색 점선, 녹색 실선과 세모기호, 파랑색 별표와 점선으로 각각의 함수를 표현
plt.plot(x, y1, 'r--', x, y2, 'g^-', x, y3, 'b*:')
plt.axis([-30,30,-30,30])   # 그림을 그릴 영역을 지정함
plt.show()
