# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_user = int(input("Введите число: "))
number_str = ''
sum_number = 0
i = 0
while i != number_user:
    number_str = int(str(number_user) + str(number_str))  # складываем число пользователя в строке и преобразуем в int
    sum_number = number_str + sum_number  # сумма чисел за один цикл
    i += 1
    print(number_str)
print(sum_number)
