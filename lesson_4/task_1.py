# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv


def calculation(hours, rate, premium):
    result = (hours * rate) + premium
    return result


try:
    script_name, hours_param, rate_param, premium_param = argv
    print(calculation(int(hours_param), float(rate_param), float(premium_param)))
except ValueError:
    print("Неверные параметры запуска")

