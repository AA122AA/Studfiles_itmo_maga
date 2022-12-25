p = int(input("Введите количество числе в группе, число должно быть простым: "))
a = []
for i in range(0, p):
    a.append((i**2)%p)
print(f"full: {a}")
print(f"Вычеты: {set(a)}")
b = [a for a in range(p)]
print(f"Невычеты: {set(b)-set(a)}")
