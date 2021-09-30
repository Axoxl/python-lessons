a = [int(x) for x in input("Введите элементы списка: ").split()]
for i in range(0, len(a) - 1, 2):
    a[i], a[i - 1] = a[i - 1], a[i]
print(a)
