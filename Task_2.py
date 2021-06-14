# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
my_file = open('test.txt', 'a', encoding='Utf-8')
line = input('Введите текст, для прекращения ввода оставьте пустую строку: ')
while line:
    my_file.write(line + '\n')
    line = input('Введите текст, для прекращения ввода оставьте пустую строку: ')
    if not line:
        break
my_file.close()
my_file = open('test.txt', 'r', encoding='Utf-8')
i_str = 0
for string in my_file:
    i_str += 1
    i_word = 0
    for word in string.split(' '):
        i_word += 1
    print(f"Количество слов в строке {i_str}: {i_word}")
print("Количество строк:", i_str)
my_file.close()
