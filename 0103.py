#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Hello python!")


# In[7]:


print("I'm so hungry")


# In[14]:


#다음 코드는 반지름을 이용하여 원의 면접을 출력하는 코드이다.
반지름 = 5 #반지름 값을 저장한다.
PI = 3.141592

면적 = PI * 반지름 ** 2 #면적을 화면에 출력한다.

print(면적)


# In[13]:


'''
안녕하세요
저는 선문대학교 1학년이고 싶은 3학년입니다.
'''


# In[15]:


2+3


# In[16]:


2*3


# In[17]:


4/2


# In[18]:


8**3


# In[19]:


8%2


# In[20]:


print("\n안녕\n잘부탁해")


# In[21]:


print("z"+"i")


# In[22]:


print("굽네"+"치킨")


# In[23]:


print("하이"*2)


# In[24]:


print("안녕'철수야'")


# In[25]:


print("300"+"200")


# In[27]:


print("ㅋ"*50)


# In[30]:


a="철수"

print(a.rjust(20))


# In[33]:


b="영희"

print(b.ljust(20))


# In[34]:


print(b.ljust(20)+a.rjust(20))


# In[36]:


weight=78.2
weight


# In[38]:


y=100
x=45
x,y


# In[39]:


x,y=100,200
result=x+y
result


# In[40]:


result=x*y
result


# In[41]:


result=(x+(y-x))
result


# In[43]:


x,y="네네","치킨"
result=(x+y)
result


# In[45]:


string_1='Hello world'
len(string_1)


# In[48]:


string_2=' Hello python'
string_1+string_2


# In[51]:


name="철수"
age=18
height=187

print("이름:",name)
print("나이:",age)
print("키:",height)


# In[55]:


money=10000000
year=5
interest=0.03

money*(1+interest)**year


# In[63]:


name="철수"
age=18
height='187'
eyesight=0.5

print(type(name))
print(type(age))
print(type(height))
print(type(eyesight))


# In[61]:


1+2==3


# In[64]:


1+2==5


# In[68]:


x=int(input("첫 번재 정수를 입력하세요: "))
y=int(input("두 번째 정수를 입력하세요: "))
s=x+y
print(x,"와",y,"의 합은",s,"입니다.")


# In[75]:


x=int(input("첫 번째 정수를 입력하세요: "))
if x<0 :
    x=int(input("양수로 입력해주세요: "))
y=int(input("두 번째 정수를 입력하세요: "))
s=x+y
print(x,"와",y,"의 합은",s,"입니다.")


# In[79]:


where=input("경기장은 어디입니까?")
win_team=input("이긴 팀은 어디입니까?")
lose_team=input("진 팀은 어디입니까?")
who=input("우수선수는 누구입니까?")
score=input("스코어는 몇대몇입니까?")
print("오늘",where,"에서 야구 경기가 열렸습니다.")
print(win_team,"와",lose_team,"은 치열한 공방전을 펼쳤습니다.")
print(who,"의 활약으로",win_team,"가",lose_team,"을",score,"로 이겼습니다.")


# In[80]:


print("소환사의 협곡에 오신 것을 환영합니다.")
cha=input("당신의 선수를 골라주십시오.: ")
print("당신은",cha,"를 선택하셨습니다.")


# In[ ]:




