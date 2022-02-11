import numpy as np

'''
a = np.array([1,2,3])   #넘파이 객체 생성
print(a.shape)  #객체의 형태
print(a.ndim)   #객체의 차원
print(a.dtype)  #객체의 내부 자료형
print(a.itemsize)   #객체의 메모리 크기(byte)
print(a.size)   #객체의 전체 크기(항목수)
'''

array_a = np.array([0,1,2,3,4,5,6,7,8,9])
print('실습1:array_a=',array_a)

array_b = np.array(range(10))
print('실습2:array_b=',array_b)

array_c = np.array(range(0,10,2))
print('실습3:array_c=',array_c)

print('실습 4: ')
print('array_c의 shape: ',array_c.shape)
print('array_c의 ndim: ',array_c.ndim)
print('array_c의 dtype: ',array_c.dtype)
print('array_c의 size: ',array_c.size)
print('array_c의 itemsize: ',array_c.itemsize)
