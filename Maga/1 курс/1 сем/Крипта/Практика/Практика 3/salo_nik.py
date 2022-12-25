from random import *

def jacobiCalc(a, n): 
    a=a%n
    res = 1
    while (a != 0):
        while (a % 2 == 0):
            a = a // 2
            tarr = [3, 5]
            if ((n % 8) in tarr):
                res = res*-1
        a, n = n, a
        if (a % 4 == n % 4 == 3):
            res = res*-1 
        a=a%n
    if (n == 1):
        return res
    return 0

def solostrassCalc(p, k=100):
    if (p == 2):
        print('Prime')
        return
    elif (p % 2 == 0):
        print('Composite')
        return
    for i in range(k):
        a = randint(1, p-1)
        jacobi_sym = (p + jacobiCalc(a, p)) % p
        e = (p - 1) // 2
        res = pow(a, e, p)
        if (jacobi_sym == 0 or res != jacobi_sym):
            print('Composite')
            return 
    print('Prime')
    return


solostrassCalc(32208088957291906505333188294626721534926077998968143162390906054269771332195153578543417)







