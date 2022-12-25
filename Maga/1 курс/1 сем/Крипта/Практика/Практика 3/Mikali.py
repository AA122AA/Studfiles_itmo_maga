c = [218, 34, 194, 164, 220, 50, 237, 77,
    68, 151, 135, 21, 101, 167, 196, 98,
    196, 219, 89, 241, 16, 134, 240, 43,
    36, 193, 37, 17, 184, 61, 81, 41,
    81, 148, 18, 172, 193, 37, 203, 233,
    244, 145, 18, 1, 121, 46, 18, 193]
p = 13
q = 19
g = [i for i in range(p)]
v = [i**2%p for i in g]
nev = set(g)-set(v)
res = []
bit = []
j = 1
for i in c:
    if i%p in v:
        bit.append('0')
    else:
        bit.append('1')
    if j%8 == 0: 
        print(bit)
        res.append(chr(int(''.join(bit), 2)))
        bit = []
    j+=1

print(res)



