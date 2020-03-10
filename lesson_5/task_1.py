# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


with open("file_1.txt", "w", encoding="utf-8") as file:
    while True:
        new_string = input("Введите новую строку: ")
        if new_string:
            print(new_string, file=file)

        else:
            break
