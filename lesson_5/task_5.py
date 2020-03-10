# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

file_name = "file_5.txt"

with open(file_name, "w", encoding="utf-8") as file:
    new_list = [str(randint(-100, 100)) for i in range(30)]
    file.write(" ".join(new_list))

with open(file_name, "r", encoding="utf-8") as file:
    sum_new = sum(int(x) for x in file.read().split(" "))
    print(f"Сумма чисел: {sum_new}")

