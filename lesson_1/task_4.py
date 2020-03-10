# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое число: "))

max_number = 0

while number:
    current_number = number % 10

    if max_number < current_number:
        max_number = current_number

    if max_number == 9:
        break

    number = number // 10

print(f"Самая большая цифра: {max_number}")
