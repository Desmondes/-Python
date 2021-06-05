#  Реализовать два небольших скрипта:
#  а) итератор, генерирующий целые числа, начиная с указанного,
#  б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#  Подсказка: использовать функцию count() и cycle() модуля itertools.
#  Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#  Необходимо предусмотреть условие его завершения.
#  Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
#  Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from sys import argv
from itertools import count, cycle

script_name, number_user = argv
my_list_result_1 = []
my_list_result_2 = []
i = 0
if number_user.isdigit():
    if int(number_user) < 20:
        for number in count(int(number_user)):
            if number < 20:
                my_list_result_1.append(number)
            else:
                break
        for el in cycle(my_list_result_1):
            if i > len(my_list_result_1) * 10 - 1:
                break
            my_list_result_2.append(el)
            i += 1
        print("Получившийся список с функцией count():", my_list_result_1)
        print("Получившийся список с функцией cycle():", my_list_result_2)
    else:
        print("Вы должные ввести число < 20.")
else:
    print("Вы должные ввести число < 20.")
