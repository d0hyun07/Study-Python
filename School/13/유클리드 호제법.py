a,b = map(int, input().split())

def gcd(n,m):
  n = int(n)
  m = int(m)
  if n>=m:
    i=m
  else:
    i=n
  for j in range(1,i+1):
    if (n%j==0)and(m%j == 0):
      gcd_v = j
  return gcd_v

# print(gcd(a, b))


def gcd_2(n, m):
    if m == 0:
        return n
    else:
        return gcd_2(m, n % m)

print(gcd_2(a, b))


