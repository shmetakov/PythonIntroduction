# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

day = 1
km = float(input("Введите результат 1-го дня: "))
goal_km = float(input("Введите целевое значение: "))

while km < goal_km:
    km = km * 1.1
    day = day + 1

print(day)
