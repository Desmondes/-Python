# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.


Greeting = "Hello"
world = "World"
number = 26
month = 'May'
print(Greeting, world, number, month)

name = input("Введите имя: ")
age = int(input("Введите возраст: "))
month_user = input("Введите название текущего месяца: ")
number_user = int(input("Введите текущее число: "))
print(f'Привет {name}, сейчас {number_user} число, {month_user} месяц, вам {age} лет.')
