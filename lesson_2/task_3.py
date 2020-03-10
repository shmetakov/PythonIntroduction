# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ["весна", "лето", "осень", "зима"]
seasons_dict = {(1, 2, 12): "зима", (3, 4, 5): "весна",
                (6, 7, 8): "лето", (9, 10, 11): "осень"}

while True:
    try:
        month = int(input("Введите номер месяца: "))

        if 0 < month <= 12:
            print(f"{month} месяц. Время года: {seasons_list[(month // 3) - 1]}")

            for key, val in seasons_dict.items():
                if key.count(month):
                    print(f"{month} месяц. Время года: {val}")
                    break
            break

        else:
            print(f"{month} - такого месяца не существует")

    except ValueError:
        print("Введено неверное значение")
    else:
        print("Еще раз...")
