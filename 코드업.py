a, b, d, c = map(int, input().split())
for i in range(c - 1):
    a = a * b + d

print(a)
