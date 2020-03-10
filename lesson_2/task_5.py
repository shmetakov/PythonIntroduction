# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]

while True:
    try:
        number = int(input("Введите число: "))

        if number >= 0:
            for i, val in enumerate(my_list, 0):
                if val < number:
                    my_list.insert(i, number)
                    break

                if (i + 1) == len(my_list):
                    my_list.append(number)
                    break
            break
        else:
            print("Число должно быть положительным")

    except ValueError:
        print("Введено неверное значение")
    else:
        print("Еще раз...")

print(my_list)
