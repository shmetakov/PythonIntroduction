# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def my_funk(x, y):
    return x ** y


def my_funk_2(x, y):
    y = abs(y)
    result = 1
    while y:
        result = result / x
        y -= 1

    return result


while True:
    try:
        x = float(input("Введите действительное положительное число x: "))
        y = int(input("Введите целое отрицательное число y: "))
    except ValueError:
        print("Введено неверное значение")
        continue

    if not x > 0:
        print("x должен быть положительным")
        continue

    if not y < 0:
        print("y должен быть отрицательным")
        continue

    print(f"{x} в степени {y} = {my_funk(x, y)}")
    print(f"{x} в степени {y} = {my_funk_2(x, y)}")

    break

