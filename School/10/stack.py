stack_size = 5

list=[None]*stack_size

top = -1

def isEmpty():
  if top == -1:
    return True
  return False

def isFull():
  if top == stack_size-1:
    return True
  return False

def push(e):
  global top
  if not isFull():
    top = top+1
    list[top] = e
    print(list[top])


def pop(e):
  if not isEmpty():
    top = top -1
    list[top] = e
    print(list[top])

def peek():
  if not isEmpty():
    list[top]
    print(list[top])

push(1)