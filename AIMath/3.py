import numpy as np

def perc(X, W, d):
  X = np.array(X)
  W = np.array(W)
  S = np.dot(X, W)
  if S >= d:
    return(1)
  else:
    return 0

#퍼셉트론
def perc_and(X):
  return(perc(X, [5,5],6))

def perc_or(X):
  return(perc(X,[5,5],4))

def perc_nand(X):
  return(1-perc_and(X))

# 다중퍼셉트론 구현(XOR)
def perc_xor(X):
  return(perc_and([perc_nand(X),perc_or(X)]))


for x in range(2):
  for y in range(2):
    print(perc_xor([x, y]))
