# a = int(input())

# for i in range(1,7):
#   for j in range(1,7):
#     if i+j == a:
#       print(i,j)

      
a,b,c = map(int,input().split())
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_3(x, y, z):
    return gcd(gcd(x, y), z)


print(gcd_3())
