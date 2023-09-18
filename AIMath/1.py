# import numpy as np

# A = {1,2,3}
# B = {1,3,4}
# print(A|B) # |로 합집합
# print(A&B) # &로 교집합
# print(len(A)) # len으로 원소 개수

# A = set("안녕, 반가워, ㅋㅋ".split(","))

# listA = set("한파,눈,예보,일부,비".split(","))
# listB = set("눈,예보,퇴근길,조심".split(","))
# listC = set("비,예보,일부,눈,그치다,한파".split(","))

# print(listA)
# print(listB)
# print(listC)

# A = {'일부', '눈', '예보', '비', '한파'}
# B = {'예보', '퇴근길', '눈', '조심'}
# C = {'일부', '눈', '예보', '비', '그치다', '한파'}
# U = A|B|C
# listU = list(U)
# print(listU)

# print(A)
# print(B)
# print(C)
# print(U)

# def Vec(X):
#   result = []
#   for t in listU:
#     if t in X:
#       result.append(1)
#     else:
#       result.append(0)
#   return(np.array(result))

# print(Vec(A))
# print(Vec(B))
# print(Vec(C))

# 한파,눈,예보,일부,비,퇴근길,조심,그치다
# VA = np.array([1, 1, 2, 1, 1, 0, 0, 0])
# VB = np.array([0, 2, 1, 0, 0, 1, 1, 0])
# VC = np.array([1, 1, 1, 1, 3, 0, 0, 1])

# print(VA)
# print(VB)
# print(VC)

# # TF
# print(VA + VB + VC)


# def Bin(X):
#     result = []
#     for i in X:
#         if i != 0:
#             result.append(1)
#         else:
#             result.append(0)
#     return np.array(result)


# # DF/n
# print((Bin(VA) + Bin(VB) + Bin(VC)) / 3)

# # IDF
# IDF = 1 / ((Bin(VA) + Bin(VB) + Bin(VC)) / 3)
# print(IDF)

# # TF*IDF
# print(VA * IDF)
# print(VB * IDF)
# print(VC * IDF)

# # IDF
# IDF = 1 / ((Bin(VA) + Bin(VB) + Bin(VC)) / 3)
# print(IDF)

# # TF*IDF
# print(VA * IDF)
# print(VB * IDF)
# print(VC * IDF)
