numb = int(input("Введите число: "))

if numb % 2 == 0:
    print(f"{numb} == четное")
else:
    print(f"{numb} == нечетное")

# дополнительное

if numb % 3 == 0:
    print(f"число {numb} делится на 3")

if numb == 0:
    print("число это 0")
elif numb >= 0:
    print(f"число {numb} положительное")
else:
    print(f"число {numb} отрицательное")