class MyCDeque:
    def __init__(self, max_size):
        self.deque = [None] * max_size
        self.front = 0
        self.rear = 0
        self.size = 0
        self.max_size = max_size

    def isempty(self):
        return self.size == 0

    def isfull(self):
        return self.size == self.max_size

    def addfront(self, item):
        if not self.isfull():
            self.front = (self.front - 1) % self.max_size
            self.deque[self.front] = item
            self.size += 1
        else:
            print("Deque is full")

    def addrear(self, item):
        if not self.isfull():
            self.deque[self.rear] = item
            self.rear = (self.rear + 1) % self.max_size
            self.size += 1
        else:
            print("Deque is full")

    def deletefront(self):
        if not self.isempty():
            item = self.deque[self.front]
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return item
        else:
            raise IndexError("Deque is empty")

    def deleterear(self):
        if not self.isempty():
            self.rear = (self.rear - 1) % self.max_size
            item = self.deque[self.rear]
            self.size -= 1
            return item
        else:
            raise IndexError("Deque is empty")

    def getfront(self):
        if not self.isempty():
            return self.deque[self.front]
        else:
            raise IndexError("Deque is empty")

    def getrear(self):
        if not self.isempty():
            return self.deque[(self.rear - 1) % self.max_size]
        else:
            raise IndexError("Deque is empty")


my_c_deque = MyCDeque(max_size=10)

my_c_deque.addfront(1)
print(my_c_deque.deque)
my_c_deque.addrear(2)
print(my_c_deque.deque)
my_c_deque.addfront(3)
print(my_c_deque.deque)
my_c_deque.addfront(4)
print(my_c_deque.deque)
my_c_deque.addfront(5)
print(my_c_deque.deque)
my_c_deque.addfront(6)
print(my_c_deque.deque)
my_c_deque.addfront(7)

print(my_c_deque.deque)
print(my_c_deque.getfront())
print(my_c_deque.getrear())

my_c_deque.deletefront()
my_c_deque.deleterear()

print(my_c_deque.deque)
