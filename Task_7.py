# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json

profit = {}
pr = {}
list_1 = []
prof = 0
prof_aver = 0
i = 0
with open('text_7.txt', 'r', encoding='Utf-8') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit[name] > 0:
            prof = prof + profit.setdefault(name)
        else:
            i -= 1
        i += 1
    prof_aver = prof / i
    pr = {'Средняя прибыль': round(prof_aver)}
    list_1.append(profit)
    list_1.append(pr)
    print(list_1)
with open('text_7.json', 'w', encoding='UTF-8') as write_js:
    json.dump(list_1, write_js, ensure_ascii=False)
