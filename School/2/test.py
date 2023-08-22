print("hello world")

a = 10
b = 15
print(a, b)

a = input()
print(a)

a = int(input("정수를 입력하세요"))
b = int(input("입력"))

print(a + b)

# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a + b)


a = True
b = False
c = a and b
d = a or b
print(not a)
while True:
    print(a)
    break
a = 10
b = 10.5
print(a + b)

a = 2
b = 3
print(a**b)


count = 0
while count != 3:
    count += 1
    print("hi")


# 파이썬 6069
a = input()

if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

# 파이썬 6070
a = int(input())

if a == 1 or a == 2 or a == 12:
    print("winter")
elif a == 3 or a == 4 or a == 5:
    print("spring")
elif a == 6 or a == 7 or a == 8:
    print("summer")
elif a == 9 or a == 10 or a == 11:
    print("fall")

# 파이썬 6073
a = int(input())

while a != 0:
    a = a - 1
    print(a)

# 파이썬 6075
a = int(input())
i = 0
while i != a:
    print(i)
    i = i + 1
print(i)

# 파이썬 6077
a = int(input())
s = 0
for i in range(1, a + 1):
    if i % 2 == 0:
        s = s + i
print(s)

# 파이썬 6079
a = int(input())
s = 0
for i in range(1, a + 1):
    s = s + i
    if s >= a:
        print(i)
        break

# 파이썬 6080
a, b = map(int, input().split())

for i in range(1, a + 1):
    for j in range(1, b + 1):
        print(i, j)

# 파이썬 6083
a, b, c = map(int, input().split())
sum = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            sum = sum + 1
            print(i, j, k)
print(sum)

# 파이썬 6088
a, b, c = map(int, input().split())
for i in range(c - 1):
    a = a + b

print(a)

# 파이썬 6089
a, b, c = map(int, input().split())
for i in range(c - 1):
    a = a * b

print(a)
