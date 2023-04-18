# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
with open('task_6.txt', 'r', encoding='utf-8') as file:
    # Создаем пустой словарь, в котором будем хранить данные
    subjects_dict = {}
    # Читаем файл построчно
    for line in file:
        # Разбиваем строку на название предмета и список занятий
        name, lessons = line.strip().split(': ')
        # Разбиваем список занятий на отдельные элементы
        lessons_list = lessons.split(' ')
        # Создаем переменные для хранения количества занятий по каждому типу
        lections = 0
        practicals = 0
        labs = 0
        # Проходим по списку занятий и суммируем количество по каждому типу
        for lesson in lessons_list:
            if '(л)' in lesson:
                lections += int(lesson.split('(л)')[0])
            elif '(пр)' in lesson:
                practicals += int(lesson.split('(пр)')[0])
            elif '(лаб)' in lesson:
                labs += int(lesson.split('(лаб)')[0])
        # Суммируем общее количество занятий по предмету
        total_lessons = lections + practicals + labs
        # Записываем данные в словарь
        subjects_dict[name] = total_lessons

# Выводим полученный словарь на экран
print(subjects_dict)