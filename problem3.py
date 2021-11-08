# Largest prime factor

num = 600851475143    
prime_factors = []

for i in range(2, num):
    if num % i == 0:
        num //= i
        prime_factors.append(i)
        i = 2
        if num == 1:
            break

print(prime_factors)
    