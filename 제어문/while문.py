### while문

"""
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
"""

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1 # treeHit+=1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")

#While문 만들기
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number:"""
number = 0
while number !=4:
    print(prompt)
    number = int(input())

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee-=1 # coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

#While문의 맨 처음으로 돌아가기

a = 0
while a < 10:
    a = a+ 1
    if a % 2 == 0: continue
    print(a)

#무한 루프
while True:
    print("Ctrl + c를 눌러야 while 문을 빠져나갈 수 있습니다.")
    