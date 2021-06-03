#  Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
#  но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func(word):
    latin = True
    for letter in word:
        if ord(letter) in range(97, 123):
            pass
        else:
            latin = False
    if latin is True:
        return word.capitalize()
    else:
        print("Слово должно состоять из маленьких латинский букв.")


result = int_func(input("Введите слово из маленьких латинских букв: "))
if result is not None:
    print(f"Результат: {result}")
