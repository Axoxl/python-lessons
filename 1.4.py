n = int(input("Введите целое число: "))
m = n % 10
n = n // 10
while n > 0:
    if not n % 10 <= m:
        m = n % 10
    n = n // 10
print(m)
