'''
< 데이터 프레임 붙이기 여러 함수 >
1. pd.concat - 데이터프레임을 병합해주는 함수
2. pd.merge - 두 데이터프레임을 각 데이터에 존재하는 고유값(key)을 기준으로 병합할 때 사용하는 함수
3. join - merge와 비슷하지만 행 인덱스를 기준으로 결합한다는 차이점이 있음.

'''
# 데이터 구조의 변경
'''
import pandas as pd
df_1 = pd.DataFrame({'item':['ring0','ring0','ring1','ring1'],
                     'type':['Gold','Silver','Gold','Bronze'],
                     'price':[20000,10000,50000,30000]})
print(df_1)
df_2 = df_1.pivot(index='item', columns='type', values='price')
print(df_2)
'''
# --------------------
# 데이터 프레임의 병합
'''
import pandas as pd
df_1 = pd.DataFrame({'A':['a10','a11','a12'],
                     'B':['b10','b11','b12'],
                     'C':['c10','c11','c12']},
                    index = ['가','나','다'])
df_2 = pd.DataFrame({'B':['b23','b24','b25'],
                     'C':['c23','c24','c25'],
                     'D':['d23','d24','d25']},
                    index = ['다','라','마'])
# df_1, df_2 두 데이터프레임을 합쳐서 df_3을 생성
df_3 = pd.concat([df_1, df_2])
print(df_3)
'''
# --------------------
# 데이터 프레임의 병합2
'''
import pandas as pd
df_1 = pd.DataFrame({'A':['a10','a11','a12'],
                     'B':['b10','b11','b12'],
                     'C':['c10','c11','c12']},
                    index = ['가','나','다'])
df_2 = pd.DataFrame({'B':['b23','b24','b25'],
                     'C':['c23','c24','c25'],
                     'D':['d23','d24','d25']},
                    index = ['다','라','마'])

print(pd.concat([df_1, df_2], axis=0, join='outer'))
print(pd.concat([df_1, df_2], axis=0, join='inner'))
print(pd.concat([df_1, df_2], axis=1, join='outer'))
print(pd.concat([df_1, df_2], axis=1, join='inner'))

# axis=0은 세로로 더해지고 axis=1은 가로로 더해짐
# outer는 합집합, inner는 교집합
'''
# --------------------

# 데이터 프레임의 병합3
'''
import pandas as pd
df_1 = pd.DataFrame({'A':['a10','a11','a12'],
                     'B':['b10','b11','b12'],
                     'C':['c10','c11','c12']},
                    index = ['가','나','다'])
df_2 = pd.DataFrame({'B':['b23','b24','b25'],
                     'C':['c23','c24','c25'],
                     'D':['d23','d24','d25']},
                    index = ['다','라','마'])
df_3 = df_1.merge(df_2, how='outer', on='B')
print(df_3)
# 합집합이기 때문에 B를 기준으로 모든 데이터가 나옴
'''
# -------------------
# 데이터 프레임의 병합4
'''
import pandas as pd

df_1 = pd.DataFrame({'A':['a10','a11','a12'],
                     'B':['b10','b11','b12'],
                     'C':['c10','c11','c12']},
                    index = ['가','나','다'])
df_2 = pd.DataFrame({'B':['b23','b24','b25'],
                     'C':['c23','c24','c25'],
                     'D':['d23','d24','d25']},
                    index = ['다','라','마'])

print('left outer \n', df_1.merge(df_2, how='left', on='B'))
print('right outer \n', df_1.merge(df_2, how='right', on='B'))
print('full outer \n', df_1.merge(df_2, how='outer', on='B'))
'''
# ---------------------
# 데이터 정렬
'''
import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('countries.csv',index_col = 0)
countries_df.sort_values(['population','area'],
                         ascending = False, inplace = True)
print(countries_df)
# ascending - 오름차순
# inplace - 기존 데이터프레임에 덮어써서 저장
'''
# ----------------------
# 데이터 정렬2
'''
import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('countries.csv',index_col = 0)
countries_df.sort_values(['population'],
                         ascending=False, inplace=True)
print(countries_df)
'''
# ---------------------

