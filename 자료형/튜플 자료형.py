#튜플

t1 = ()
t2 = (1,)#요소가 하나일땐 요서 뒤에 ,(콤마)를 무조건 붙혀야함
t3 = (1,2,3)
t4 = 1,2,3 #괄호 생략 가능
t5 = ('a','b', ('ab','cd'))

#인덱싱
t1 = (1,2,'a','b')
print(t1[0])
print(t1[3])

#슬라이싱
t1 = (1,2,'a','b')
print(t1[1:])

#튜플 더하기
t1 = (1,2,'a','b')
t2 =(3,4)
t3 = t1 + t2
print(t3)

#튜플 곱하기
t2 = (3,4)
t3 = t2 * 3
print(t3)

#튜플 길이 구하기
t1 = (1,2,'a','b')
print(len(t1))