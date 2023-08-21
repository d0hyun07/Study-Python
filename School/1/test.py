a = int(input())
b = 0
for i in range(1,a+1):
    if i%2==0:
        b+=i

print(b)

n = int(input())
def fib(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr

print(fib(n))