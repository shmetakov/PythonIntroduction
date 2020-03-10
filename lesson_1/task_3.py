# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    n = int(input("Введите чило от 0 до 9: "))
    if 0 <= n <= 9:
        break

    print("Еще раз...")

result = n + int(str(n) * 2) + int(str(n) * 3)

print(f"n + nn + nnn = {result}")
