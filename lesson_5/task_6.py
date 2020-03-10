# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

new_dict = dict()


def get_sum(line):
    new_list = [i for i in line if i.isdigit() or i == " "]
    return sum(int(x) for x in "".join(new_list).split(" ") if not x == "")


with open("task_6.txt", "r", encoding="utf-8") as file:
    for line in file:
        new_dict[line[:line.find(":")]] = get_sum(line[line.find(":") + 2:])

print(new_dict)
