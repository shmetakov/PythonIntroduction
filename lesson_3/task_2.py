# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.


def func(first_name, second_name, city, year, phone, email):
    result = f"имя = {second_name}, фамилия = {first_name}, год рождения = {year}, "
    result += f"город проживания = {city}, email = {email}, телефон = {phone}"
    print(result)


s_name = input("Введите имя: ")
f_name = input("Введите фамилию: ")
year = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите email: ")
phone = input("Введите номер телефона: ")

func(second_name=s_name, first_name=f_name, year=year, city=city, email=email, phone=phone)
