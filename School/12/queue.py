stack_size = 5
list=[None]*stack_size
top=-1

def isEmpty():
  if top==-1: return True
  else: return False

def isFull():
  return top==stack_size-1

def push(e):
  global tmp
  if not isFull():
    tmp = tmp+1
    list[top] = e
    print(list)