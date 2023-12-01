class Stack:
  def __init__(self):
    # 생성자: 스택 요소를 저장할 빈 리스트 초기화
    self.items = []

  def is_empty(self):
    # 스택이 비어있는지 확인
    return len(self.items) == 0

  def push(self, item):
    # 스택의 맨 위에 항목을 추가
    self.items.append(item)

  def pop(self):
    # 스택의 맨 위에서 항목을 제거하고 반환
    if not self.is_empty():
      return self.items.pop()
    else:
      # 스택이 비어있으면 IndexError 발생
      raise IndexError("빈 스택에서 pop 시도")

  def peek(self):
    # 스택의 맨 위에 있는 항목을 제거하지 않고 반환
    if not self.is_empty():
      return self.items[-1]
    else:
      # 스택이 비어있으면 IndexError 발생
      raise IndexError("빈 스택에서 peek 시도")

  def size(self):
    # 스택의 요소 개수 반환
    return len(self.items)

# 사용 예시:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("스택 크기:", stack.size())  # 출력: 3
print("스택 맨 위:", stack.peek())  # 출력: 3

popped_item = stack.pop()
print("빠져나온 항목:", popped_item)  # 출력: 3
print("pop 후 스택 크기:", stack.size())  # 출력: 2
