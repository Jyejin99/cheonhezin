# csv파일 불러오기
'''
import csv

f = open('weather.csv')
data = csv.reader(f)
header = next(data)     # 헤더의 제거
for row in data:
    print(row)
f.close()
'''
# --------------------------
'''
import csv

max_temp = 0.0
date = ''

f = open('weather.csv') # csv 파일을 열어서 f에 저장한다.
data = csv.reader(f)    # reader() 함수를 이용하여 읽는다.
header = next(data)     # 헤더의 제거
for row in data:
    if max_temp < float(row[2]):
        max_temp = float(row[2])
        date = row[0]
        
print("5월 중", date,"가", max_temp, "로 가장 덥습니다.")
f.close()
'''
# --------------------------
# pandas 모듈을 이용한 데이터 분석 기초
'''
import numpy as np
import pandas as pd

series = pd.Series([1,3,4,np.nan,6,8])
print(series)

# --------------------------

import numpy as np
import pandas as pd

king_s = pd.Series(["태조","정종","태종","세종","문종","단종"])
Crowning_day_s = pd.Series([1392, 1398, 1400, 1418, 1450, 1452])
name_s = pd.Series(["이성계","이방과","이방원","이도","이향","이흥휘"])
dethronement_s=pd.Series([1398,1400,1418,1450,1452,1455])
print(king_s, Crowning_day_s, name_s, dethronement_s)
'''
# -------------------------
# 데이터 구조의 변경
'''
import numpy as np
import pandas as pd

king_s = pd.Series(["태조","정종","태종","세종","문종","단종"])
Crowning_day_s = pd.Series([1392, 1398, 1400, 1418, 1450, 1452])
name_s = pd.Series(["이성계","이방과","이방원","이도","이향","이흥휘"])
dethronement_s=pd.Series([1398,1400,1418,1450,1452,1455])

df = pd.DataFrame({'묘호':king_s, '즉위':Crowning_day_s,
                   '이름':name_s, '폐위':dethronement_s})

print(df)
'''
# ------------------------
# 한글 깨짐 해결
'''
import pandas as pd

df = pd.read_csv('weather.csv',index_col = 0, encoding='CP949')
print(df)
'''
# ------------------------
# 엑셀 파일 원하는 열만 가져오기
'''
import pandas as pd

df = pd.read_csv('weather.csv', index_col = 0, encoding='CP949')
print(df[['날짜','온도']])
'''
# ------------------------
# 나라별 인구 차트
'''
import pandas as pd
import matplotlib.pyplot as plt

contries_df = pd.read_csv('countries.csv', index_col=0)
contries_df['population'].plot(kind='bar', color=('b','darkorange','g','r','m'))
plt.show()
'''
# ------------------------
'''
# 나라별 인구 차트2

import pandas as pd
import matplotlib.pyplot as plt

contries_df = pd.read_csv('countries.csv', index_col=0)
contries_df['population'].plot(kind='pie')
plt.show()
'''
# ------------------------
# hist 차트
'''
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('weather2.csv',index_col=0, encoding='CP949')
weather['풍속(m/s)'].plot(kind='hist',bins=100)
plt.show()
'''
# -------------------------
# describe - 데이터를 자세하게 보여주는 것
'''
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('weather2.csv', index_col=0, encoding='CP949')
weather['풍속(m/s)'].plot(kind='hist',bins=33)

print(weather.describe())

plt.show()
'''
# --------------------------
# describe 외에 데이터 유형을 보여주는 여러 함수들
'''
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('weather2.csv', index_col=0, encoding='CP949')
weather['풍속(m/s)'].plot(kind='hist',bins=33)

print(weather.describe())
print(weather.mean())
print(weather.std())

plt.show()
'''
# ---------------------------
# 날짜별로 데이터 분리하여 그래프 만들기
'''
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('year_weather.csv', encoding='CP949')
monthly = [None for x in range(12)]
monthly_temp = [0 for x in range(12)]

weather['day']=pd.DatetimeIndex(weather['날짜']).month

for i in range(12):
    monthly[i] = weather[weather['day']==i+1]
    monthly_temp[i] = monthly[i].mean()['평균기온(℃)']

plt.plot(monthly_temp, 'red')
plt.show()
'''
# ---------------------------
'''
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('year_weather.csv', encoding='CP949')
weather['평균기온(℃)'].plot()
weather['최저기온(℃)'].plot()
weather['최고기온(℃)'].plot()
plt.show()
'''
# ----------------------------
# 그룹으로 만들어서 그래프 만들기
'''
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('year_weather.csv', encoding='CP949')

weather['month']=pd.DatetimeIndex(weather['날짜']).month
means = weather.groupby('month').mean()

print(means)

means['평균기온(℃)'].plot(kind='bar')
plt.show()
'''
# -----------------------
'''
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('year_weather.csv', encoding='CP949')

weather['month']=pd.DatetimeIndex(weather['날짜']).month
means = weather.groupby('month').mean()

print(weather['평균기온(℃)']>=25)   # <--이렇게 쓰면 아무것도 안 나옴
print(weather[weather['평균기온(℃)']>=25])   # <--이렇게 쓰면 나옴
'''
# -----------------------
# 데이터 삭제 및 수정
'''
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('year_weather.csv',encoding='CP949')
missing_data = weather[weather['평균기온(℃)'].isna()]    #isna는 Na를 True로 출력하는 함수
print(missing_data)
'''
# ------------------------
# 데이터 삭제 및 수정2
'''
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('year_weather.csv', encoding='CP949')
missing_data = weather[weather['평균기온(℃)'].isna()]
print(missing_data)
weather.fillna(0,inplace=True)      # fillna는 결측값 대체하는 함수임
missing_data = weather[weather['평균기온(℃)'].isna()]
print(missing_data)
'''
# -----------------------
# 데이터 삭제 후 재저장
'''
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('year_weather.csv', encoding='CP949')
missing_data = weather[weather['평균기온(℃)'].isna()]
print(missing_data)
weather.fillna(0,inplace=True)      
missing_data = weather[weather['평균기온(℃)'].isna()]
print(missing_data)

weather.to_csv("test_modified.csv", sep=",", index = False, encoding='CP949')
'''

