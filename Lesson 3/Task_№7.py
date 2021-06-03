#  Продолжить работу над заданием.
#  В программу должна попадать строка из слов, разделенных пробелом.
#  Каждое слово состоит из латинских букв в нижнем регистре.
#  Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
#  Необходимо использовать написанную ранее функцию int_func().
def int_func(word):
    latin = True
    for letter in word:
        if ord(letter) in range(97, 123):
            pass
        else:
            latin = False
    if latin is True:
        return word[0].upper() + word[1:].lower()
    else:
        print("Слово должно состоять из маленьких латинский букв.")


user_list = input().split()
for element in user_list[:]:  # использую срез что бы не перепрыгивало значения
    letter = int_func(element)
    if letter is None:  # если значение введено не верно, то его удаляю
        user_list.remove(element)
    else:
        user_list.insert(user_list.index(element), letter)  # добавляю новое значение и удаляю старое
        user_list.remove(element)
print(' '.join(user_list))  # привожу к списку
