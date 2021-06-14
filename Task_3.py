# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
my_file = open('text_3.txt', 'r', encoding='Utf-8')
income = 0
worker = 0
for string in my_file:
    worker += 1
    profit = string.split(' ')[1]
    if float(profit) < 20000:
        print(f"Доход меньше 20000 имеет: {string.split(' ')[0]}")
    income += float(profit)
print(f"Средняя величина дохода сотрудников: {income / worker}")
my_file.close()
