def dec(encarr, p=13, q=19):
    res = []
    for c in encarr:
        c=c%p
        residues = list(set([i**2 % p for i in range(p)])) 
        nonresidues = set(range(p)).difference(residues) 
        if c in residues:
            res.append('0') 
        else:
            res.append('1') 
    for pt in res:
        print(pt, end='') 
    print()
    return

ena = [218, 34, 194, 164, 220, 50, 237, 77] 
dec(ena)
ena = [68, 151, 135, 21, 101, 167, 196, 98]
dec(ena)
ena = [196, 219, 89, 241, 16, 134, 240, 43]
dec(ena)
ena = [36, 193, 37, 17, 184, 61, 81, 41]
dec(ena)
ena = [81, 148, 18, 172, 193, 37, 203, 233]
dec(ena)
ena = [244, 145, 18, 1, 121, 46, 18, 193]
dec(ena)
