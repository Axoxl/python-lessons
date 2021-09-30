list1 = [2, 9, 1, 5]
a = input("введите целое натуральное число")
for i in list1:
    if a == 2:
        print(list1.insert(1, a))
    if a == 9:
        print(list1.insert(2, a))
    if a == 1:
        print(list1.insert(3, a))
    if a == 5:
        print(list1.insert(4, a))
    else:
        print(list1, a)
