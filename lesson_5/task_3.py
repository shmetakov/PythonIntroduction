# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников


with open("task_3.txt", "r", encoding="utf-8") as file:
    name_list = ""
    arg_salary = 0
    i = 0

    try:
        for new_line in file:
            name, salary = new_line.split()
            if float(salary) < 20000:
                name_list += f"{name}\n"

            arg_salary += float(salary)
            i += 1

        print("Сотрудники с окладом менее 20 тыс:")
        print(name_list)
        arg_salary = arg_salary / i
        print(f"Средняя величина дохода сотрудников: {arg_salary:.2f}")

    except ValueError:
        print("Некорректные данные в файле")
