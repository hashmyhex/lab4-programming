import math

a = float(input("введите a: "))
b = float(input("введите b: "))
c = float(input("введите c: "))

if a == 0:
    print("это не квадратное уравнение")
else:
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"два корня: x1 == {x1:.2f}, x2 == {x2:.2f}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"один корень: x == {x:.2f}")
    else:
        print("нет действительных корней")
