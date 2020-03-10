class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))

    if b == 0:
        raise MyZeroDivisionError("Деление на 0")

except MyZeroDivisionError as err:
    print(err)
except ValueError:
    print("Вы ввели не число")
else:
    print(f"{a} / {b} = {a / b}")