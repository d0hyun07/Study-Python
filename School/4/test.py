# # num = 85
# # type(num)

# # foo = 100
# # type(foo)

# ### 진법 바꾸기

# print(0o10)

# print(0x10)

# print(0b10)

# ### float

# print(0.4e7)
# print(4.2e-4)

### 코드업

# d=[]                        #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
# for i in range(20) :
#   d.append([])         #리스트 안에 다른 리스트 추가해 넣기
#   for j in range(20) :
#     d[i].append(0)    #리스트 안에 들어있는 리스트 안에 0 추가해 넣기

# n = int(input())
# for i in range(n) :
#   x, y = input().split()
#   d[int(x)][int(y)] = 1

# for i in range(1, 20) :
#   for j in range(1, 20) :
#     print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
#   print()                          #줄 바꿈

# d=[]

# for i in range(20) :
#   d.append([])         #리스트 안에 다른 리스트 추가해 넣기
#   for j in range(20) :
#     d[i][j] = input().split()

# n = input()
# for i in range(n) :
#   x,y=input().split()
#   for j in range(1, 20) :
#     if d[j][int(y)]==0 :
#       d[j][int(y)]=1
#     else :
#       d[j][int(y)]=0

#     if d[int(x)][j]==0 :
#       d[int(x)][j]=1
#     else :
#       d[int(x)][j]=0

#   for i in range(1, 20) :
#     for j in range(1, 20) :
#       print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
#     print()

# d=[]
# for i in range(20) :
#   d.append([])
#   for j in range(20) :
#     d[i].append(0)

# for i in range(19) :
#   a = input().split()
#   for j in range(19) :
#     d[i+1][j+1] = int(a[j])

# n = int(input())
# for i in range(n) :
#   x,y=input().split()
#   x=int(x)
#   y=int(y)
#   for j in range(1, 20) :
#     if d[j][y]==0 :
#       d[j][y]=1
#     else :
#       d[j][y]=0

#     if d[x][j]==0 :
#       d[x][j]=1
#     else :
#       d[x][j]=0

# for i in range(1, 20) :
#   for j in range(1, 20) :
#     print(d[i][j], end=' ')
#   print()


# 설탕 과자 뽑기

# list = []
# h, w = int(input().split())
# for i in range(h + 1):
#     list.append([])
#     for j in range(w + 1):
#         list[i].append(0)

# n = int(input())

# for i in range(n + 1):
#     l, d, x, y = map(int(input().split()))
#     for j in range(l + 1):
#         if d == 0:
#             list[x][y] = 1
#             x += 1
#         elif d == 1:
#             list[x][y] = 1
#             y += 1


# for i in range(h + 1):
#     for j in range(w + 1):
#         print(list[i][j], end=" ")
#     print()
