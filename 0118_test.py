
# 데이터 분석 실습1

#1
import pandas as pd
import numpy as np

car_1 = pd.read_csv('car.csv')
print(car_1)

#2
car_1.set_index('name', drop=True, append=True, inplace=True)
print(car_1)

#3
print(car_1[car_1['power']==car_1['power'].max()])

#4
car_1["mam"]=car_1["power"]*car_1["efficiency"]
print(car_1[car_1["mam"]==car_1["mam"].max()])


# ---------------------------
# 데이터 분석 실습2

#1
car_2 = pd.DataFrame({
    'name' : ['Tivoil','Korando','Rexton'],
    'power': [163,170,202],
    'weight': [1360,1470,2180],
    'efficiency': [12.0,11.3,11.1]})
print(car_2)

#2
car_2.set_index('name', drop=True, append=True, inplace=True)
print(car_1)

#3
car_3 = pd.concat([car_1,car_2])
car_2["mam"]=car_2["power"]*car_2["efficiency"]
car_3["mam"] = pd.concat([car_1["mam"],car_2["mam"]])
print(car_3)

#4
print(car_3[car_3["mam"]==car_3["mam"].max()])

