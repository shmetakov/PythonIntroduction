# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from count_script import get_numbers_list
from cycle_script import get_new_list

try:
    start_number = int(input("Введите начальное число для списка: "))
    finish_number = int(input("Введите конечное число для списка: "))

    print(get_numbers_list(start_number, finish_number))
except ValueError:
    print("Число должно быть целым")

try:
    string = input("Введите строку для повторения: ")
    finish_number = int(input("Введите конечное число для списка: "))

    print(get_new_list(string, finish_number))
except ValueError:
    print("Число должно быть целым")
