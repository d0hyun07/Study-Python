#codeup1610\
# a = input()
# b,c = map(int,input().split())
# print(a[b:b+c])


#codeup1278
# n = int(input())
# cnt = 0

# while n>0:
#   n = n//10
#   cnt = cnt + 1
# print(cnt)

#codeup1362
# n = int(input())

# def get_max_num(n):
#     num = 0
#     for i in range(1, n+1):
#         num += i
#     return num

# number = get_max_num(n)
# for i in range(1, n+1):
#     for j in range(0, i):
#         print(number, end=' ')
#         number -= 1
#     print()

#codeup1620
# n=int(input())
# s=0
# while(s==0 or s>=10): #두자리 수일 때만 돌기
#     s=0
#     while(n>0):
#         s+=int(n%10)
#         n = int(n/10)
#     n=s
# print(s)

#codeup1708
a = int(input())
b = list(map(int, input().split()))
c = sorted(b, reverse=True)
for i in range(a):
      print(b[i],c.index(b[i])+1)
#codeup2001

# pasta = []
# juice = []

# for i in range(3):
#   pasta.append(int(input()))

# for i in range(2):
#   juice.append(int(input()))

# res = (min(pasta) + min(juice)) * 1.1

# print(f'{res:.1f}')

#codeup1361
# n= int(input())
# b = n
# for i in range(n):
#   for i in range(b,n):
#     print(' ')
#     b = b-1
#   print("**\n")

# codeup2009
# a,b = map(int,input().split())
# count = 0

# while a>b-1:
#   a = a-b+1
#   count = count+1
# print(count)