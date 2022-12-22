p = int(input("Введите количество числе в группе, число должно быть простым: "))
a = []
for i in range(1, p):
    a.append((i**2)%p)
print(f"full: {a}")
print(set(a))
