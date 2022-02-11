import string

src_str = string.ascii_uppercase
dst_str = src_str[3:]+src_str[:3]

def cipher(a):
    idx = src_str.index(a)
    return dst_str[idx]

def restore(b):
    idx = dst_str.index(b)
    return src_str[idx]

src = input('문장을 입력하시오: ')
print('암호화된 문장: ', end='')

for ch in src:
    if ch in src_str:
        print(cipher(ch), end='')
    else:
        print(ch, end='')
        
print()

src2= input('복호화할 암호를 입력하시오: ')
print('복호화된 문장: ',end='')

for ch2 in src2:
    if ch2 in dst_str:
        print(restore(ch2), end='')
    else:
        print(i, end='')

print()
