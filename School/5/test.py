# stairNumber = input()
# dpList=[0]*(stairNumber)
# stairScore = [int(input()) for _ in range(stairNumber)]

# if len(stairScore)<=2:
#   print(sum(stairScore))
# else:
#   dpList[0]=stairScore[0]
#   dpList[1] = stairScore[1]+stairScore[0]

# for i in range(2, stairNumber):
#   dpList[i] = max(dpList[i-3]+stairScore[i-1],dpList[i-2]+stairScore[i])
# print(dpList[-1])


def jump(stairScore, i):
    if i < 0:
        return 0
    if i == 0:
        return stairScore[0]
    if i == 1:
        return stairScore[0] + stairScore[1]
    
    return max(jump(stairScore, i-3) + stairScore[i-1],
               jump(stairScore, i-2) + stairScore[i])

stairNumber = int(input())
stairScore = [int(input()) for _ in range(stairNumber)]

if stairNumber <= 2:
    print(sum(stairScore))
else:
    result = max(jump(stairScore, stairNumber-1),
                 jump(stairScore, stairNumber-2))
    print(result)
