###변수

a = [1,2,3]
print(id(a))

#리스트 복사
a = [1,2,3]
b = a[:]
print(id(a))
print(id(b))
print(a is b)

b = a.copy()

print(b)

#변수를 만드는 여러가지 방법
a,b = ('python','life')
(a,b) = 'python','life'
[a,b] = ['python', 'life']
a = b = 'python'

a = 3
b = 5
a, b = b, a
print(a)
print(b)