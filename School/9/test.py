'''
import time
import random

WORD_LIST=[
  "아무 문장이나 적으세요",
  "코딩하는 하루 되세요",
  "여러분 화이팅",
  "오늘 급식 뭐죠?"
]

random.shuffle(WORD_LIST)

for i in WORD_LIST:
  start_time = time.time()
  user_input = str(input(i + '\n')).strip()
  end_time = time.time()-start_time

  correct = 0
  for index, c in enumerate(user_input):
    if index >= len(i):
      break
    if c==i[index]:
      correct += 1

  total_len = len(i)
  c=correct/total_len*100
  e=(total_len-correct)/total_len*100
  speed=correct / end_time * 60

  print("속도 : {:0.2f} 정확도 : {:0.2f} 오타율 {:0.2f}".format(speed,c,e))



'''




'''
1. 클래스 붕어빵틀 = 서로 관련된 요소(변수, 기능)들을 한곳에 모아 관리하기 위한 틀
2. 객체: 클래스를 이용해 만들어진 실체
class name:
  def __init__(self,...):
          속성 정의
'''


class bssm:
  def __init__(self,name,role):
    self.school = '부소마고'
    self.age = 17
    self.role = role
    self.name = name

    


  def intro(self):
    print("안녕하세요, %s 에서 %s를 담당하고 있는 %d살 %s입니다."
          %(self.school,self.role,self.age,self.name))
    
a = bssm('wdasd','asdaw')

print(a)