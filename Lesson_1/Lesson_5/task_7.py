# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о
# фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
import json

with open('task_7.txt', encoding='utf-8') as f:
    lines = f.readlines()

profit = {}
loss = {}
total_profit = 0
count_profit = 0

for line in lines:
    name, form, revenue, cost = line.split()
    profit_value = float(revenue) - float(cost)
    if profit_value >= 0:
        profit[name] = profit_value
        total_profit += profit_value
        count_profit += 1
    else:
        loss[name] = profit_value

if count_profit > 0:
    avg_profit = total_profit / count_profit
else:
    avg_profit = 0

result = [profit, {'average_profit': avg_profit}]
with open('task_7.json', 'w') as f:
    json.dump(result, f)
