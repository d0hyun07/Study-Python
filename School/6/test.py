
# def func(*a):
  # return type(*a)

# print(func(1,2,3,4,5,5))

#codeup1901
# def count(a):
#   if a != 1:
#     count(a-1)
#   print(a)

# count(int(input()))


#codeup1902
# def count(a):
#   print(a)
#   if a != 1:
#     count(a-1)

# count(int(input()))

#codeup1904
# def count(a,b):
#   if a>b:
#     return
#   if a%2!=0:
#     print(a)
#   count(a+1,b)

# a,b = map(int, input().split())
# count(a,b)

# codeup1912

# def count(a):
#   if a<=1:
#     return 1
#   return a*count(a-1)

# a = int(input())
# print(count(a))

# def count(a):
#   if a<1:
#     return
#   count(a//2)
#   print(a%2, end="")

# a = int(input())

# if a>0:
#   count(a)
# else:
#   print("0", end="")

# codeup1953
# def t(x):
#   if x==1:
#     return '*'
#   return t(x-1)+'\n'+'*'*x

# n = int(input())
# print(t(n))

# codeup1405
# n = int(input())
# a = list(map(int, input().split()))

# for i in range(n):
#   for j in range(n):
#     print(a[i+j-n],end=' ')
#   print()

a = list(map(int, input().split()))

