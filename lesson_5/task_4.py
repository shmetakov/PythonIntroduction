# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

number_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task_4.txt", "r", encoding="utf-8") as file:
    content = file.read()
    for key, val in number_dict.items():
        content = content.replace(key, val)

    with open("new_task_4.txt", "w", encoding="utf-8") as new_file:
        print(content, file=new_file)
