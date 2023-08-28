n = int(input())
a = map(input().split())

for i in range(n):
    a[i] = int(a[i])

odd = []
for i in range(24):
    odd.append(0)

for i in range(n):
    odd[a[i]] = odd[a[i]] + 1

for i in range(1, 24):
    print(odd[i], end=" ")

### 역순 출력 ###
for i in reversed(range(1, 24)):
    print(odd[i], end=" ")
