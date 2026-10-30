a = float(input("введите сторону a: "))
b = float(input("введите сторону b: "))
c = float(input("введите сторону c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("равносторонний треугольник")
    elif a == b or a == c or b == c:
        print("равнобедренный треугольник")
    else:
        print("разносторонний треугольник")
else:
    print("треугольник не существует")
