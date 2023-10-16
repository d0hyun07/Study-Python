list_test = [1,2,3,4,5]
result = 0

for i in range(1,6):
  result = result + list_test.pop()

print(result)