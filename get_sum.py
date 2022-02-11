def get_sum(start,end):
    s=0
    for i in range(start, end+1):
        s+=i
    return s

print(get_sum(1,10))

x=get_sum(1,10)
print('x=',x)

y=get_sum(1,20)
print('y=',y)
