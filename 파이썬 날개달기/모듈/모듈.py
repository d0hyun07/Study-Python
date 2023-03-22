### 모듈

#모듈 사용 방법

import mod1 #다른 .py파일 가져옴
print(mod1.add(3,4))
print(mod1.sub(4,2))

from mod1 import add
print(add(3,4))

#if _name_ == "_main_":의 의미
#mod1.py참고

import mod1

print(mod1.add(3, 4))
print(mod1.sub(4, 2))

# 클래스나 변수 등을 포함한 모듈

import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))

print(mod2.add(mod2.PI,4.4))


