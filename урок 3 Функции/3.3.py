# Реализовать функцию my_func(), которая принимает
# три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def sum_elem1(a, b, c):
    return sum(sorted([a, b, c], reverse=True)[:2])


def sum_elem2(a, b, c):
    return sum([a, b, c]) - min([a, b, c])


print(sum_elem1(2, 5, 7))
print(sum_elem2(2, 5, 7))


