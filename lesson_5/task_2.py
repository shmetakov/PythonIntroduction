# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("file_2.txt", "a+", encoding="utf-8") as file:
    print("Новая строка", file=file)
    print("Новая строка", file=file)
    file.seek(0)

    content = file.readlines()
    print(f"Количество строк: {len(content)}")

    for i, val in enumerate(content, 0):
        print(f"Количество слов в {i + 1:3d} строке: : {len(val.split()):3d}. Строка: \"{val.rstrip()}\" ")
