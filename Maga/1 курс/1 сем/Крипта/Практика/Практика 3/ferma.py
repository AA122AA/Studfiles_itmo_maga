from random import *

n = int(input("введите число: "))
k = int(input("Количество тестов: "))
isPrime = True
if n % 2 == 0:
    print("Составное")
    exit(0)
for i in range(k):
    a = randint(1, n-1)
    if (a**(n-1))%n != 1:
        isPrime = False

if isPrime:
    print("Простое")
else:
    print("Составное")

