n=29329
row = []
d = 2
while d * d <= n:
    if n % d == 0:
        row.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    row.append(n)
print(row)
