import sympy as sp
import numpy as np
a = sp.Symbol("a")

X = np.array([-2 ,-1 ,0 ,1 ,2])
Y = np.array([-1,-3,0,3,1])


exp_a = a*X
err_a = Y - exp_a

La = sum((err_a)**2)/len(err_a)
La.expand()

# 미분
La_d = La.diff("a")

# 방정식 풀이 f = 0 을 찾는다
solves = sp.solve(La_d)

# 원래 식 대입

for i in solves:
  print(La.subs(a, i))

La = 2*a**2-4*a+4

# 수치미분
def D(c):
  h = (0.1)**6
  return ((La.subs(a, c+h)-La.subs(a, c-h))/(2*h))


la_d = La.diff("a")
#학습률 결정
c=3
r = 0.4


for n in range(100):
  #시작점, 미분계수 조사
  dc = D(c)
  print(La_d.subs(a,c))

  # 다음 점 이동
  c = c - r*dc
#  print(f"{n}번째 이동한 점 {c:.4f}")
#  print(f"{n}번째 값 {La.subs(a,c):.4f}")