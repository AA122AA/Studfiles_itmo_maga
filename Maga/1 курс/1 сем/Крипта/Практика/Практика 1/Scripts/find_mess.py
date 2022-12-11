import gmpy2
c = 16469
n = 29329
e = 17
p = 139
q = 211
d = gmpy2.invert(e, (p-1)*(q-1))
m = pow(c,d,n)
print(m)
