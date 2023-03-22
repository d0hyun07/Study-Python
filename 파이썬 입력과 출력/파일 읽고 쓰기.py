### 파일 읽고 쓰기

# f = open("새파일.txt", 'w')
# f.close()

# f = open("C:/doit/새파일.txt", 'w')
# f.close()

# 쓰기 모드
#writedata.py
# f = open("C:/doit/새파일.txt", 'w')
# for i in range(1, 11):
    # data = "%d번째 줄입니다.\n" % i
    # f.write(data)
# f.close()

# for i in range(1, 11):
    # data = "%d번째 줄입니다.\n" % i
    # print(data)

#readline 함수 이용하기
#readline_test.py
# f = open("C:/doit/새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# while True:
#    line = f.readline()
#    if not line: break
#    print(line)
#f.close()

#while True:
#    data = input()
#    if not data: break
#    print(data)

# f = open("C:/doit/새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
    # print(line)
# f.close()

# f = open("C:/doit/새파일.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# f = open("C:/doit/새파일.txt", 'r')
# for line in f:
    # print(line)
# f.close()

# f = open("C://doit/새파일.txt",'a')
# for i in range(11,20):
    # data = "%d번째 줄입니다.\n" % i
    # f.write(data)
# f.close()

# with문과 함께 사용해보기
f = open("foo.txt",'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
