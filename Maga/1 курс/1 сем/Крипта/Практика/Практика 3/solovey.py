from random import *
import math

def jacobi(a, n):
    a = a % n
    res = 1
    while (a != 0):
        while (a % 2 == 0):
            a = a // 2
            tarr = [3, 5]
            if ((n % 8) in tarr):
                res *= -1
        a, n = n, a
        if (a % 4 == n % 4 == 3):
            res *= -1
        a = a % n
    if (n == 1):
        return res
    return 0




n = int(input("введите число: "))
k = int(input("Количество тестов: "))
isPrime = True
if n == 2:
    print("Прсотое")
    exit(0)

if n % 2 == 0:
    print("Составное")
    exit(0)

for i in range(k):
    a = randint(1, n-1)
    if math.gcd(a,n) > 1:
        isPrime = False
        break
    s = pow(a,(n-1)//2, n)
    j = jacobi(a,n)
    m = (n+j)%n
    if s != m:
        isPrime = False
        break

if isPrime:
    print("Простое")
else:
    print("Составное")
