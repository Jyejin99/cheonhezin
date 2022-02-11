import numpy as np

'''
heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]
weights = [86, 74, 59, 95, 80, 68]

np_heights = np.array(heights)
np_weights = np.array(weights)

bmi = np_weights/(np_heights**2)
print('대상자들의 키:', np_heights)
print('대상자들의 몸무게:', np_weights)
print('대상자들의 BMI')
print(bmi)
'''
# --------------------------------------------
'''
x = np.array( [['a', 'b', 'c', 'd'],
               ['c', 'c', 'g', 'h']])

mat_a = np.array([[10,20,30], [10,20,30]])
mat_b = np.array([[2,2,2], [1,2,3]])

print(x [x=='c'])
print(mat_a - mat_b)
'''
# --------------------------------------------
# 슬라이싱
'''
x = np.array([[1.83, 1.76, 1.69, 1.86, 1.77, 1.73],
             [86.0, 74.0, 59.0, 95.0, 80.0, 68.0]])
y = x[0:2, 1:3] # 0:2는 두 줄 모두 선택, 1:3은 두 줄 전체의 1에서 2
z = x[0:2][1:3] 

print('x shape:',x.shape)
print('y shape:',y.shape)
print('z shape:',z.shape)
print('z shape:',z)

bmi = x[0]/x[1]**2
print('BMI data')
print(bmi)
'''
# ----------------------------------------------
'''
print(np.arange(5))
print(range(5))
print(np.array(range(5)))
print(np.arange(1,6))
print(range(1,6))
print(np.array(range(1,6)))
print(np.arange(1,10,2))
print(range(1,10,2))
print(np.array(range(1,10,2)))
'''
# -------------------------------------------------
'''
print(np.linspace(0,10,100))
print(np.logspace(0,10,100))
'''
# -------------------------------------------------
'''
y = np.arange(12)
print(y)

y = y.reshape(3,4) #행과 열
print(y)

y = y.reshape(6,-1) #-1 = 자동
print(y)

y = y.flatten()
print(y)
'''
# --------------------------------------------------
'''
print("seed is none")
print(np.random.seed(100))
print("rand is")
print(np.random.rand(100))
print("rand's start and stop")
print(np.random.rand(5,3))
print("randint is")
print(np.random.randint(1,7,size=10))
m = 175
sigma = 10
heights = m+sigma*np.random.randn(10000)
print("mean and median test")
print(heights)
print("mean is")
print(np.mean(heights))
print("median is")
print(np.median(heights))
'''
# -----------------------------------------------------

'''
players = np.zeros((100,3))
players[:,0]=10*np.random.randn(100)+175
players[:,1]=10*np.random.randn(100)+70
players[:,2]=np.floor(10*np.random.randn(100))+22

heights = players[:,0]
print("신장 평균값:", np.mean(heights))
print("신장 중앙값:", np.median(heights))

weights = players[:,1]
print("체중 평균값:", np.mean(weights))
print("체중 중앙값:", np.median(weights))

ages = players[:,2]
print('나이 평균값:',np.mean(ages))
print('나이 중앙값:',np.median(ages))
'''
