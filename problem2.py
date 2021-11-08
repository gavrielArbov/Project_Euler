# Even Fibonacci numbers

previous = 0
current = 1
total = 0

while total < 4000000:
  temp = current
  current = previous + current
  if current % 2 == 0:
    total += current
  previous = temp

print(total)

