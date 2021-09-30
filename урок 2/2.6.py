a = input("Введите название товара")
b = input("Введите цену товара")
c = input("Введите количество товара")
e = input("Введите единицу измерения товара")
my_goods = dict(name=a, price=b, count=c, mes=e)
for i, my_goods in enumerate(my_goods, 1):

    print(my_goods)
