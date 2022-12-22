import math

def isPrime(a):
    _a=a
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            print("Число должно быть простым")
            _a = getnum()
            break
    return _a

def getnum():
    a = isPrime(int(input(f"Простое число: ")))
    return a

def sansara(p,n):
    while len(p) < n:
        a = getnum()
        if (a not in p):
            p.append(a)
        else:
            print("Число должно быть уникальным")
            sansara(p,n)
    return p

def main():
    q = isPrime(int(input("Введите q: ")))
    p = []
    n = int(input("Количество простых уникальных чисел: "))
    p = sansara(p, n)
    
    if q!=2*math.prod(p)+1:
        exit("q не совпадает с введенными p")

    z=[i for i in range(2,q)]
    for i in range(len(p)):
        for j in range(len(z)):
            if pow(z[j],p[i],q)==1:
                print(f"При ord(a{i+1})=p{i+1}, a = {z[j]}, p{i+1}={p[i]}") 
                break 

if __name__ == "__main__":
    main()