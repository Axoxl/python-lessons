a = input("Введите номер месяца: ")
ds = {"s": [6, 7, 58]}
dsp = {"sp": [3, 4, 5]}
dau = {"au": [3, 4, 5]}
wd = {"w": [3, 4, 5]}
for i in ds:
    if i == a:
        print("лето")
for i in wd:
    if i == a:
        print("зима")
for i in dsp:
    if i == a:
        print("весна")
for i in dau:
    if i == a:
        print("осень")