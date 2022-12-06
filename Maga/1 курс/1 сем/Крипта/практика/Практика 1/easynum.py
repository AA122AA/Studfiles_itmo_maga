n=1000
primes = []
for target_num in range(1, n):
    is_prime = True
    for i in range(2, target_num):
        if target_num % i == 0:
            is_prime = False
    if is_prime:
        primes.append(target_num)
print([i%4 for i in primes])
