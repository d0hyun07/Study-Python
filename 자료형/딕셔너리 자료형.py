###딕셔너리

dic ={'name':'pey', 'phone':'010-9999-1234','birth':'1118'}
a = {1:'hi'}
a = {'a':[1,2,3]}

#딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1,2,3]
print(a)

#딕셔너리 요소 삭제
del a[1]#Key에 해당하는 쌍이 삭제된다.
print(a)

#딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey' : 10, 'julliet' : 99}
print(grade['pey'])
print(grade['julliet'])

a = {1:'a',2:'b'}
print(a[1])
print(a[2])

a = {'a':1,'b':2}
print(a['a'])
print(a['b'])

#딕셔너리 만들 때 주의할 사항
a = {1:'a', 1:'b'}#Key가 중복되었을 때 1개를 제외한 나머지 값이 모두 무시됨
print(a)
#튜플은 Key로 쓸 수 있지만 리스트는 요소값이 바뀔 수 있기 때문에 불가능함

#딕셔너리 관련 함수
a = {'name':'pey','phone':'010-9999-1234', 'birth': '1118'}
print(a.keys())#Key 리스트 만들기
for k in a.keys():
    print(k)

print(list(a.keys()))#Key를 리스트로 변환

print(a.values())#Value 리스트 만들기

print(a.items()) #Key,Value 쌍 얻기

a.clear() #Key,Value 쌍 모두 지우기(None = 거짓)

a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print(a.get('name'))#Key로 Value얻기
print(a.get('phone'))
print(a.get('nokey', 'foo'))

a = {'name':'pey','phone':'010-9999-1234', 'birth': '1118'}
print('name' in a)#해당 Key가 딕셔너리 안에 있는지 조사
print('email' in a)



