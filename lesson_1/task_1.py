# Поработайте с переменными, создайте несколько, выведите на экран, запросите у
# пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

int_number = 5
float_number = 63.7
my_str = "Привет, Мир!"
my_bool = True

print(int_number)
print(float_number)
print(my_str)
print(my_bool)

print("int_number = %d, float_number = %.2f" % (int_number, float_number))

print("my_str = '{}'".format(my_str))
print("float_number = {:.1f}".format(float_number))

print(f"int_number = {int_number}, my_bool = {my_bool}")

input_int_number = int(input("Введите целое число тип (int): "))
input_float_number = float(input("Введите вещественное число (float): "))
input_str = input("Введите сторку: ")

print(f"Вы ввели целое число {input_int_number}")
print(f"Вы ввели вещественное число {input_float_number}")
print(f"Вы ввели сторку '{input_str}'")
