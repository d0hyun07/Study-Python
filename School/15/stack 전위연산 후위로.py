class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    else:
      print("스택이 비어 있습니다.")

  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    else:
      print("스택이 비어 있습니다.")

  def size(self):
    return len(self.items)

def is_operator(char):
  # 주어진 문자가 연산자인지 확인한다.
  return char in "+-*/^"

def infix_to_postfix(infix_expr):
  stack = Stack()
  postfix_result = []
  precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

  for char in infix_expr:
    if char.isalnum():
      # Operand인 경우 결과 리스트에 추가합니다.
      postfix_result.append(char)
    elif char == '(':
      # 여는 괄호인 경우 스택에 푸시합니다.
      stack.push(char)
    elif char == ')':
      # 닫는 괄호인 경우 여는 괄호가 나올 때까지 스택에서 팝하여 결과 리스트에 추가합니다.
      while not stack.is_empty() and stack.peek() != '(':
        postfix_result.append(stack.pop())
      stack.pop()  # 여는 괄호를 제거
    elif is_operator(char):
      # 연산자인 경우 스택에 있는 연산자 중 현재 연산자보다 우선순위가 높거나 같은 것들을 결과 리스트에 추가하고, 현재 연산자를 스택에 푸시합니다.
      while not stack.is_empty() and stack.peek() != '(' and is_operator(stack.peek()) and precedence[stack.peek()] >= precedence[char]:
        postfix_result.append(stack.pop())
      stack.push(char)

  # 스택에 남아 있는 모든 연산자를 결과 리스트에 추가합니다.
  while not stack.is_empty():
    postfix_result.append(stack.pop())

  # 최종적으로 조합된 postfix 표현을 문자열로 반환합니다.
  return ''.join(postfix_result)

# Infix expression input
infix_expr = "A+B*C-(D/E+F)*G"

# Convert infix to postfix
postfix_expr = infix_to_postfix(infix_expr)

print(f"Infix expression: {infix_expr}")
print(f"Postfix expression: {postfix_expr}")
