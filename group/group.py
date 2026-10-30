try:
    radius = float(input("введите радиус: "))
    tochka_x = float(input("введите точку X: "))
    tochka_y = float(input("введите точку Y: "))

    if radius <= 0:
        print("радиус должен быть больше нуля")
    elif tochka_x**2 + tochka_y**2 <= radius**2:
        print("точка попадает в круг")
    else:
        print("точка НЕ попадает в круг")
except ValueError:
    print("ошибка!!! надо только цифры")
