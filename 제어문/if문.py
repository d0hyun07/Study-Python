### if문

money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

"""
if 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
else:
    수행 할 문장A
    수행 할 문장B

--------------------------------

비교 연산자
x < y : x가 y보다 작다.
x > y : x가 y보다 크다.
x == y : x와 y가 같다.
x != y : x와 y가 같지 않다.
x >= y : x가 y보다 크거나 같다.
x <= y : x가 y보다 작거나 같다. 
"""

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

"""
x or y : x와 y둘중에 하나만 참이여도 참이다
x and y : x와 y 모두 참이어야 참이다.
not x : x가 거짓이면 참이다
"""

money = 2000
card = True
if money >= 3000 or card:# 둘중 하나만 참이여도 참
    print("택시를 타고 가라")
else:
    print("걸어가라")

"""
x in 리스트 |  x not in 리스트
x in 튜플   |  x not in 튜플
x in 문자열 |  x not in 문자열
"""

print(1 in [1,2,3])
print(1 not in [1,2,3])
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#조건문에서 아무일도 하지 않게 설정하는법

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
#elif는 이전 조건문이 거시일 때 수행된다.
pocket = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

#조건부 표현식
score = 60
message = "success" if score >= 60 else "failure"
print(message)






