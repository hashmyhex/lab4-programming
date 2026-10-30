a = float(input("введите первое число: "))
b = float(input("введите второе число: "))
operation = input("введите операцию (+, -, *, /): ").strip()

match operation:
    case "+":
        print(f"результат == {a + b}")
    case "-":
        print(f"результат == {a - b}")
    case "*":
        print(f"результат == {a * b}")
    case "/":
        if b == 0:
            print("ошибка: деление на ноль")
        else:
            print(f"результат == {a / b:.2f}")
    case _:
        print("неизвестная операция")
