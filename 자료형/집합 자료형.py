###집합

s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

s = set()

#집합 자료형의 특징
"""
중복을 허용하지 않는다.
순서가 없다(Unordered)
"""

s1 = set([1,2,3]) 
l1 = list(s1)
print(l1)
print(l1[0])
t1 = tuple(s1)
print(t1)
print(t1[0])#인덱싱으로 접근하려면 리스트나 튜플로 바꿔야함

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#교집합
print(s1 & s2)
print(s1.intersection(s2))

#합집합
print(s1 | s2)
print(s1.union(s2))

#차집합
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

#집합 자료형 관련 함수들
s1 = set([1,2,3])
s1.add(4)#값 1개 추가하기
print(s1)

s1 = set([1,2,3])
s1.update([4,5,6])#값 여러 개 추가하기
print(s1)

s1 = set([1,2,3])# 특정 값 제거하기
s1.remove(2)
print(s1)