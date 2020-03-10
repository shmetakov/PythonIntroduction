# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(numerator, denominator):
    result = numerator / denominator
    return result


while True:
    try:
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))

        print(division(a, b))

        break
    except ValueError:
        print("Введено неверное значение")
        
    except ZeroDivisionError:
        print("Деление на 0")

