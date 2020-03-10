# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce


def my_func(prev_i, i):
    return prev_i * i


new_list = [i for i in range(100, 1001) if i % 2 == 0]

print(new_list)
print(reduce(my_func, new_list))
