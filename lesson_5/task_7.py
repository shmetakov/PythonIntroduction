# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json

list_profit = []
firm_dict = dict()

with open("task_7.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, type_firm, profit, costs = line.split(" ")
        profit = int(profit) - int(costs)

        if profit > 0:
            list_profit.append(profit)

        firm_dict[name] = profit

json_list = [firm_dict, {"average_profit": (sum(list_profit) / len(list_profit))}]

print(json_list)

with open("task_7.json", "w", encoding="utf-8") as json_file:
    json.dump(json_list, json_file, ensure_ascii=False, indent=4)

