###codeup1413
string = input()
for i in range(len(string)-1, -1, -1):
    print(string[i], end='')


### codeup1617

class ReverseNumber:
    def __init__(self):
        num = int(input())
        print(self.reverse(num))
        sum = num + self.reverse(num)
        print(f"'{sum}'")
        length = len(str(sum))
        if length == 1:
            print("YES")
        elif length == 2:
            if sum % 10 == sum // 10:
                print("YES")
            else:
                print("NO")
        elif length == 3:
            if sum % 10 == sum // 100:
                print("YES")
            else:
                print("NO")
        elif length == 4:
            if sum % 10 == sum // 1000 and (sum // 10) % 10 == (sum // 100) % 10:
                print("YES")
            else:
                print("NO")
    @staticmethod
    def reverse(num):
        result = 0
        while num != 0:
            result = result * 10 + num % 10
            num //= 10
        return result
ReverseNumber()