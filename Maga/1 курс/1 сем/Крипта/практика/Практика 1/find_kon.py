a = 370864
divs = []
b = 2
while a > 1:
    while a%b != 0:
        b+=1
    divs.append(b)
    a /= b
    b = 2
print(divs)
