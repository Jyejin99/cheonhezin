# global 함수 사용하기

def print_counter():
    global counter
    counter=200
    print('counter=', counter)

counter=100
print_counter()
print('counter=',counter)
