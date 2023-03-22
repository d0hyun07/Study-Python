###리스트


odd = [1, 3, 5, 7, 9]

#리스트명 =[요소1, 요소2, 요소3, ...]


#리스트 생김새
a = []
b = [1,2,3]
c = ['life', 'is', 'too', 'short']
d = [1,2, 'life','is']
e = [1,2,['Life', 'is']]

a = list()#비어있는 리스트는 이렇게 생성할 수 있음

#리스트의 인덱싱, 슬라이싱
a = [1,2,3]
print(a[0] + a[2])

a = [1,2,3,['a','b','c']]
print(a[-1])
print(a[3])

print(a[-1][0])
print(a[-1][1])
print(a[-1][2])
#리스트 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])
b = a[:2]
c = a[2:]
print(b)
print(c)

a = [1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])

#리스트 연산
a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a * 3)

#리스트 길이 구하기
a = [1,2,3]
print(len(a))

#리스트 수정과 삭제
a = [1,2,3]
a[2] = 4
print(a)

#del함수
a = [1,2,3]
del a[1]
print(a)
#객체: 파이썬에서 사용되는 모든 자료형
a = [1,2,3,4,5]
del a[2:]
print(a)

#리스트 관련 함수들
a = [1,2,3]
a.append(4)#리스트 맨 마지막에 괄호 안을 추가
print(a)
a.append([5,6])
print(a)

a = [1,4,3,2]
a.sort()#리스트의 요소를 정렬함
print(a)
a = ['a','c','b']
a.sort()
print(a)

a = ['a','c','b']
a.reverse()#리스트를 뒤집는다
print(a)

a = [1,2,3]
print(a.index(3))#인덱스 반환(괄호 안의 것이 리스트 안에 없으면 오류가 뜸)
print(a.index(1))

a = [1,2,3]
a.insert(0, 4)#리스트에 요소 삽입
print(a)
a.insert(3, 5)
print(a)

a = [1,2,3,1,2,3]
a.remove(3)#리스트 요소 제거(리스트에서 첫번째로 나오는 괄호 안에 것을 삭제함)
print(a)
a.remove(3)
print(a)

a = [1,2,3]
a.pop()#리스트 요소 끄집어 내고 삭제
print(a)
a = [1,2,3]
a.pop(1)#괄호안이 비어있다면 맨 마지막을 끄집어내고 삭제함
        #괄호안에 수가 있으면 그 번째의 요소를 끄집어내고 삭제함
print(a)

a = [1,2,3,1]
print(a.count(1))#리스트에 포함된 요소 x의 개수 세기

a = [1,2,3]
a.extend([4,5])#리스트를 확장
print(a)
a.extend([6,7])
print(a)

