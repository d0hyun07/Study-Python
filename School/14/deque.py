class MyDeque:
  def __init__(self):
    self.deque = []
    self.max_size = 10

  def isempty(self):
    return len(self.deque) == 0

  def isfull(self):
    return len(self.deque) == self.max_size

  def size(self):
    return len(self.deque)

  def addfront(self, item):
    if not self.isfull():
      self.deque.insert(0, item)
    else:
      print("Deque is full")

  def addrear(self, item):
    if not self.isfull():
      self.deque.append(item)
    else:
      print("Deque is full")

  def deletefront(self):
    if not self.isempty():
      return self.deque.pop(0)
    else:
      raise IndexError("Deque is empty")

  def deleterear(self):
    if not self.isempty():
      return self.deque.pop()
    else:
      raise IndexError("Deque is empty")

  def getfront(self):
    if not self.isempty():
      return self.deque[0]
    else:
      raise IndexError("Deque is empty")

  def getrear(self):
    if not self.isempty():
      return self.deque[-1]
    else:
      raise IndexError("Deque is empty")

my_deque = MyDeque()

my_deque.addfront(1)
print(my_deque.deque)
my_deque.addrear(2)
print(my_deque.deque)
my_deque.addfront(3)
print(my_deque.deque)
my_deque.addfront(4)
print(my_deque.deque)
my_deque.addfront(5)
print(my_deque.deque)
my_deque.addfront(6)
print(my_deque.deque)
my_deque.addfront(7)

print(my_deque.deque)
print(my_deque.getfront())
print(my_deque.getrear())

my_deque.deletefront()
my_deque.deleterear()

print(my_deque.deque)
