# Largest palindrome product

list = []
for i in range(900, 1000):
    for j in range(900, 1000):
        num = i * j
        if num%10 == num//100000 and num//10%10 == num//10000%10 and num//100%10 == num//1000%10:
            list.append(num)

print(list)