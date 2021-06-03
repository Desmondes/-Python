#  Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(val_1, val_2):
    try:
        return val_1 / val_2
    except ZeroDivisionError:
        print("Деление на 0!")


quotient = division(float(input('Введите делимое: ')), (float(input('Введите делитель: '))))
if quotient is None:
    print("Невозможная операция!")
else:
    print(f"Ответ: {quotient}")
