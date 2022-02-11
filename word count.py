t="There's a reason some people are working to make it harder to vote, especially for people of color. It's because when we show up, things change."

'''
world_list = t.split()
word_count={}

for word in world_list:
    word_count[word] = word_count.get(word,0)+1
    keys = sorted(word_count.keys())
for word in keys:    
    print(word,':', str(word_count[word]))
'''

length = len(t.split(' '))
print('word count:', length)

user = input("빈도를 세고 싶은 문자를 적어주세요.: ")
answer = t.count(user)
print(user,":",answer,"개")
