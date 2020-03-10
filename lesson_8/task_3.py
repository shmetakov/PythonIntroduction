class MyValueError(Exception):
    def __init__(self, txt):
        self.txt = txt


new_list = []

while True:
    try:
        input_str = input("Введите число: ")

        if input_str == "stop":
            print(f"Введены числа: {new_list}")
            break

        if not input_str.isdigit():
            raise MyValueError(f"Вы ввели не число: {input_str}")
        else:
            new_list.append(int(input_str))

    except MyValueError as err:
        print(err)
