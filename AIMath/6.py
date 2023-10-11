import sympy as sp
import numpy as np
a = sp.Symbol("a")


listx = np.array([3,6,9,3,6,9])
listy = np.array([5,8,11,3,4,5])

# expect1 = (9/8)*listx
# expect2 = (7/8)*listx
# expect3 = listx
# expecta = a*listx

# print(expecta)

# dist1 = listy - expect1
# dist2 = listy - expect2
# dist3 = listy - expect3
# dista = listy - expecta

# print(sum(dist1**2)/len(listx))
# print(sum(dist2**2)/len(listx))
# print(sum(dist3**2)/len(listx))
# sp.expand(sum(dista**2)/len(listx)) # 손실함수

def lof( X, Y,a):
  listx = np.array(X)
  listy = np.array(Y)
  expecta = a*listx
  dista = listy - expecta
  return sp.expand(sum(dista**2)/len(listx))


lof1 = lof(listx,listy,a)
lof1

print(lof1.subs(a, 4/3))
print(lof1.subs(a, 2/3))
print(lof1.subs(a, 1))
print(lof1.subs(a, 5/3))
print(lof1.subs(a, 5/6))
print(lof1.subs(a, 1/3))