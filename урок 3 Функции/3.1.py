# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def del_fun(a, b):
    if b == 0:
        print("на ноль делить нельзя")
    else:
        print(a / b)


del_fun(int(input("Введите первое число")), int(input("Введите второе число")))
