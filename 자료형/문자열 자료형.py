###문자열

food = "python's favorite food is perl" #작은 따옴표에 작은 따옴표를 포함시키면 오류가 남"""
say = '"Python is very easy." he says.'
say2 = "\"Python is very easy.\" he says."#따옴표를쓰고 싶을땐 \(역슬래시)" or '를 쓰면 된다.
multiline = 'Life is too short.\nYou need python'#줄바꿈하고 싶으면 \n
multiline2 = '''
Life is too short
You need python
''' # 큰 따옴표 가능



print(food)
print(say)
print(say2)
print(multiline)
print(multiline2)


### 문자열 연산

head = "Python"
tail = " is fun!"
print(head + tail)

a = "python"
print(a*2)

### 응용(multistring.py)

print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short"
len(a) # 문자열 길이 구하기

#문자열 인덱싱(파이썬은 0부터 센다)
a[0]
a[-1]# 뒤에서부터
a[3]#앞에서 부터

# 문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
print(a[10:])
print(a[:17])
print(a[:])
print(a[19:-7])

#슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date =a[:8]
weather = a[8:]
print(date)
print(weather)

#문자열 바꾸기 

#a = "Pithon"
#a[1]
#print(a)
#a[1] ='y'
#print(a)(오류가 생긴다)

a = "Pithon"
print(a[:1] + 'y' + a[2:])



#포매팅

print("I eat %d apples." % 3) #숫자대입
print("I eat %s apples."% "five")#문자열 대입

number = 3
print("I eat %d apples." % number)
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days" % (number,day))
print("Error is %d%%" % 98)#%를 쓸땐 %%를 쓰면 된다.


#포맷 코드와 숫자 함께 사용하기
print("%10s"%"hi")
print("%-10sjane"%"hi")
print("%0.4f"%3.42134234)
print("%10.4f"%3.42134234)

#format함수를 사용한 포매팅
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
number = 3
print("I eat {0} apples".format(number))
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))#위 두개를 섞어 쓸 수도 있음


#정렬

print("{0:<10}".format("hi"))#왼쪽 정렬
print("{0:>10}".format("hi"))#오른쪽 정렬
print("{0:^10}".format("hi"))#가운데 정렬

print("{0:=^10}".format("hi"))#정렬할 때 공백문자 대신에 다른 기호도 넣을 수 있다.
#소수점 표현
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))#정렬과 소수점 둘다 같이 가능함

print("{{ and }}".format())#중괄호를 넣고 싶을땐 연속으로 사용하면 된다.

#f 문자열 포매팅
name = '강도현'
age = 17
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name':'강도현', 'age':17}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

#정렬

print(f'{"hi":<10}')#왼쪽 정렬
print(f'{"hi":>10}')#오른쪽 정렬
print(f'{"hi":^10}')#가운데 정렬
print(f'{"hi":=^10}')# 공백채우기 가능함

#소수점 표현
y = 3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')#정렬 가능
print(f'{{ and }}')# 중괄호 사용하려면 연속으로 사용하면 됨


#문자열 관련 함수들
a = "Python is the best choice"
print(a.count('t'))#문자 개수 세기
print(a.find('b'))#위치 알려주기 (존재하지 않으면 -1을 출력함)

print(a.index('t'))#위치 알려주기2 (존재하지 않으면 오류남)
print(",".join('abcd'))#문자열 삽입
a = "hi"
print(a.upper())#소문자 대문자로 바꾸기
a = "HI"
print(a.lower())#대문자 소문자로 바꾸기
a = " hi "
print(a.lstrip())#왼쪽 공백 지우기
print(a.rstrip())#오른쪽 공백 지우기
print(a.strip())#양쪽 공백 지우기

a = "Life is too short"
print(a.replace("Life", "Your leg"))# 문자열 바꾸기
print(a.split())#문자열 나누기
b = "a:b:c:d"
print(b.split(':'))