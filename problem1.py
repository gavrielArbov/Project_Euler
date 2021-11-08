# Multiples of 3 and 5

below = 1000
arr = [3, 5]
list = []
sum = 0
for x in range(below):
  if x % arr[0] == 0 or x % arr[1] == 0:
    list.append(x)

for x in list:
  sum += x

print(sum)