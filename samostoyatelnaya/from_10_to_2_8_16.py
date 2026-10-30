try:
    vvedenoe_chislo = int(input("введите исходное число из десятичной системы: "))
    alph = int(input("в какую систему счисления перевести? "))

    match alph:
        case 2:
            print(
                f"{vvedenoe_chislo} в {alph}-ричной системе счисления = {vvedenoe_chislo:b}"
            )
        case 8:
            print(
                f"{vvedenoe_chislo} в {alph}-ричной системе счисления = {vvedenoe_chislo:o}"
            )
        case 16:
            print(
                f"{vvedenoe_chislo} в {alph}-ричной системе счисления = {vvedenoe_chislo:x}"
            )
        case _:
            print(f"не хочу измерять в {alph}-ричной системе счисления")

except ValueError:
    print("ошибка: нужно ввести целое число!")
