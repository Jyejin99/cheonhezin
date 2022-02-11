# 선형 그래프
'''
import matplotlib.pyplot as plt

x = [x for x in range(20)]
y = [x**2 for x in range(20)]
z = [x**3 for x in range(20)]

plt.plot(x, x, label='linear')
plt.plot(x, y, label='quadratic')
plt.plot(x, z, label='qubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("My Plot")
plt.legend()
plt.show()
'''
# -------------------------------
# 선형 그래프2
'''
import math
import matplotlib.pyplot as plt

x = []
y = []

for angle in range(360):
    x.append(angle)
    y.append(math.sin(math.radians(angle)))

plt.plot(x,y)
plt.title("SINE WAVE")
plt.show()
'''
# --------------------------------

# 세로 막대 그래프
'''
from matplotlib import pyplot as plt

# 1인당 국민소득
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]

plt.bar(range(len(years)), gdp)

plt.title("GDP per capita") #제목을 설정한다.
plt.ylabel("dollars")   #y축에 레이블을 붙인다.

# y축에 틱을 붙인다.
plt.xticks(range(len(years)), years)
plt.show()
'''
# --------------------------------

# 세로 막대 그래프2
'''
from matplotlib import pyplot as plt
import numpy as np

# 1인당 국민소득
years = [1965, 1975, 1985, 1995, 2005, 2015]
ko = [130, 650, 2450, 11600, 17790, 27250]
jp = [890, 5120, 11500, 42130, 40560, 38780]
ch = [100, 200, 290, 540, 1760, 7940]

x_range = range(len(years))
plt.bar(x_range, ko, width = 0.25)
plt.bar(x_range, jp, width = 0.25)
plt.bar(x_range, ch, width = 0.25)

plt.title("GDP per capita")
plt.ylabel("dollars")

# y축에 틱을 붙인다.
plt.xticks(range(len(years)), years)
plt.show()

x_range = np.arange(len(years))
plt.bar(x_range + 0.0, ko, width = 0.25)
plt.bar(x_range + 0.3, jp, width = 0.25)
plt.bar(x_range + 0.6, ch, width = 0.25)

plt.title("GDP per capita")
plt.ylabel("dollars")

# y축에 틱을 붙인다.
plt.xticks(range(len(years)), years)
plt.show
'''
# -----------------------------------
# 산점도 그래프
'''
import matplotlib.pyplot as plt
import numpy as np

xData = np.arange(20, 50)
# xData에 randn() 함수로 잡음을 섞는다.
# 잡음은 정규분포로 만들어 짐
yData = xData + 2*np.random.randn(30)

plt.scatter(xData, yData)
plt.title('Real Age vs Physical Age')
plt.xlabel('Real Age')
plt.ylabel('Physical Age')

plt.savefig("age.png", dpi=600)
plt.show()
'''
# -------------------------------
# 원형 그래프
'''
import matplotlib.pyplot as plt
times = [8, 14, 2]

timelabels = ["Sleep", "Study", "play"]

# autopct로 백분율을 표시할 때 소수점 2번째 자리까지 표시
# labels 매개 변수에 timelabels 리스트를 전달
plt.pie(times, labels = timelabels, autopct = "%.2f")
plt.show()
'''
# -------------------------------
# 히스토리 그래프
'''
import numpy as np
import matplotlib.pyplot as plt

n_bins = 10
x = np.random.randn(1000)
y = np.random.randn(1000)

plt.hist(x, n_bins, histtype='bar', color = 'red')
plt.hist(y, n_bins, histtype='bar', color = 'blue', alpha=0.3)
plt.show()
'''
# -----------------------------
# 히스토리 그래프2
'''
import numpy as np
import matplotlib.pyplot as plt

mu1, sigma1 = 10, 2
mu2, sigma2 = -6, 3

standard_Gauss = np.random.randn(10000)
Gauss1 = mu1 + sigma1 * np.random.randn(10000)
Gauss2 = mu2 + sigma2 * np.random.randn(10000)

plt.figure(figsize=(10,6))
plt.hist(standard_Gauss, bins=50, alpha=0.4)
plt.hist(Gauss1, bins=50, alpha=0.4)
plt.hist(Gauss2, bins=50, alpha=0.4)

plt.show()
'''
# -----------------------------
# 박스 그래프
'''
import numpy as np
import matplotlib.pyplot as plt

random_data = np.random.randn(100)

plt.boxplot(random_data)
plt.show()
'''
# --------------------------------
# 박스 그래프2
'''
import numpy as np
import matplotlib.pyplot as plt

data1 = [1,2,3,4,5]
data2 = [2,3,4,5,6]

plt.boxplot([data1, data2])
plt.show()

plt.boxplot(np.array([data1, data2]))
plt.show()
'''
# ---------------------------------
# 한번에 다양한 그래프를 표현하기

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5,5))

axs[0,0].hist(data[0])
axs[1,0].scatter(data[0], data[1])
axs[0,1].plot(data[0], data[1])
axs[1,1].hist2d(data[0], data[1])

plt.show()

