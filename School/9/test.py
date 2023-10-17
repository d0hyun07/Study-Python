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
'''

for i in enumerate(['A','B','C']):
  print(i)