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
        a = a % n
    if (n == 1): 
        return res
    return 0

print(jacobiCalc(48489,1231231))
