# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds_user = int(input("Введите время в секундах: "))
hour = seconds_user // 3600
minutе = seconds_user // 60 % 60
seconds = seconds_user % 60
print(f'Получится {hour} часов {minutе} минут {seconds} секунд.')
