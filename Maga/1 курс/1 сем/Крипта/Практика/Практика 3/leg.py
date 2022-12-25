def isPrime(a):
    a = int(a)
    return all(a % i for i in range(2, a))

def factorize(n):
    factors = []

    p = 2
    while True:
        while n % p == 0 and n > 0:  # while we can divide by smaller number, do so
            factors.append(p)
            n = n / p
        p += 1  # p is not necessary prime, but n%p == 0 only for prime numbers
        if p > n / p:
            break
    if n > 1:
        factors.append(n)
    return factors


def calculateLegendre(a, p):
    if a >= p or a < 0:
        return calculateLegendre(a % p, p)
    elif a == 0 or a == 1:
        return a
    elif a == 2:
        if p % 8 == 1 or p % 8 == 7:
            return 1
        else:
            return -1
    elif a == p - 1:
        if p % 4 == 1:
            return 1
        else:
            return -1
    elif not isPrime(a):
        factors = factorize(a)
        product = 1
        for pa in factors:
            product *= calculateLegendre(pa, p)
        return product
    else:
        if ((p - 1) / 2) % 2 == 0 or ((a - 1) / 2) % 2 == 0:
            return calculateLegendre(p, a)
        else:
            return (-1) * calculateLegendre(p, a)
a5 = []
a7 = []
a35 = []
b = []
for i in range(35):
   a5.append(int(calculateLegendre(i,5)))
   a7.append(int(calculateLegendre(i,7)))
   a35.append(int(calculateLegendre(i,35)))
   b.append(f"{i}: {int(calculateLegendre(i,5))}, {int(calculateLegendre(i,7))}, {int(calculateLegendre(i,35))}")
   
for i in range(len(b)):
    print(b[i])
