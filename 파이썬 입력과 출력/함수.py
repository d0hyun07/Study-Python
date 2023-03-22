### 함수

def add(a,b):  #a, b는 매개변수
    return a+b      
print(add(3,4)) # 3, 4는 인수


a = 3
b = 4
c = add(a,b)
print(c)

"""
일반적인 함수

def 함수이름(매개변수):
    <수행할 문장>
    ...
    return 리턴값
"""

def add(a, b):      #입력값 없는 함수
    result = a + b
    return result

def say():          #리턴값 없는 함수
    return 'Hi'

a = say()
print(a)

def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a,b,a+b))

print(add(3, 4))
print(a)

def say():          #입력값 리턴값 다 없는 함수
    print('Hi')
print(say())

def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)

result = sub(b=5, a=3)
print(result)

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
result = add_mul('add',1,2,3,4,5)
print(result)

result = add_mul('mul',1,2,3,4,5)
print(result)

# 키워드 매개변수 kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print(print_kwargs(a=1))

print(print_kwargs(name='foo',age=3))

def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result)

def add_and_mul(a,b):
    return a+b
    return a*b     # 실행 안됨 

def say_nick(nick):
    if nick == "바보":
        return  # return을 단독으로 써서 함수를 즉시 빠져나갈 수 있음
    print("나의 별명은 %s 입니다." % nick)

print(say_nick('야호'))
print(say_nick('바보'))

#매개변수에 초깃값 미리 설정
def say_myself(name, age, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

print(say_myself("박응용", 27))
print(say_myself("박응용", 27, True))
print(say_myself("박응선", 27, False))

# vartest
a = 1
def vartest(a):
    a = a+1

vartest(a)
print(a)

def vartest(hello):
    hello = hello+1

#함수 안에서 함수 밖의 변수를 변경하는 방법

# 1. return 사용하기
a = 1
def vartest(a):
    a = a+1
    return a

a = vartest(a)
print(a)

# 2. global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a+1

vartest()
print(a)

# lambda
add = lambda a,b: a+b
result = add(3, 4)
print(result)

def add(a,b):
    return a+b
result = add(3,4)
print(result)            #2개가 같음



