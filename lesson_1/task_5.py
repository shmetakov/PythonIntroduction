# Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = float(input("Введите значение выручки: "))
cost = float(input("Введите значение издержки: "))

profit = revenue - cost

if profit > 0:
    print(f"Прибыль фирмы составила: {profit:.2f}")
    print(f"Рентабельность выручки: {(profit / revenue):.2f}")

    employees = int(input("Введите численность сотрудников фирмы: "))

    print(f"Прибыль фирмы в расчете на одного сотрудника: {(profit / employees):.2f}")

elif profit == 0:
    print(f"Прибыль нулевая")

else:
    print(f"Убыток фирмы составил: {profit:.2f}")