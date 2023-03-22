### for문

"""
기본구조

for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...

"""

#1. 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#2. 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

#3. for문의 응용
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


#for문과 continue
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

#for문과 함께 자주 사용하는 range 함수
a = range(10)
print(a)
a = (1,11)#끝숫자는 포함 X

add = 0
for i in range(1,11):
    add = add + i

print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다."% (number+1))

#for와 range를 이용한 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print('')

#리스트 컴프리헨션 사용하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]#[표현식 for 항목 in 반복가능객체 if 조건문]
print(result)
"""
[표현식 for 항목1 in 반복가능객체1 if 조건문1
        for 항목2 in 반복가능객체2 if 조건문2
        ...
        for 항목n in 반복가능객체n if 조건문n]
"""

result = [x*y for x in range(2,10)
              for y in range(1,10)]

print(result)