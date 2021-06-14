# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
rus = {'Fizra:': 'Физкультура', 'Math:': 'Математика', 'History:': 'История', 'Physics:': 'Физика',
       'Informatics:': 'Информатика', 'Literature:': 'Литература', 'Russian:': 'Русский'}
subj = {}
with open('text_6.txt', 'r', encoding='Utf-8') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        lecture = lecture.replace('(л)', '')
        practice = practice.replace('(пр)', '')
        lab = lab.replace('(лаб)', '')
        if lecture != '-':
            lecture = int(lecture)
        else:
            lecture = 0
        if practice != '-':
            practice = int(practice)
        else:
            practice = 0
        if lab != '-':
            lab = int(lab)
        else:
            lab = 0
        subj_f = {rus[subject]: lecture + practice + lab}
        subj.update(subj_f)
print("Общее количество часов:")
print(subj)
