# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт
# средней величины дохода сотрудников.
with open('task_3.txt', encoding='utf-8') as file:
    # Инициализируем переменные
    total_income = 0
    count = 0
    low_income_employees = []

    # Читаем файл построчно
    for line in file:
        # Разбиваем строку на фамилию и оклад
        name, income = line.strip().split()

        # Преобразуем оклад в число с плавающей точкой
        income = float(income)

        # Добавляем оклад к общей сумме доходов
        total_income += income

        # Увеличиваем счётчик сотрудников
        count += 1

        # Если оклад меньше 20000, добавляем фамилию в список
        if income < 20000:
            low_income_employees.append(name)

    # Выводим список сотрудников с низким окладом
    print("Сотрудники с окладом менее 20000: ", low_income_employees)

    # Вычисляем средний доход
    average_income = total_income / count

    # Выводим средний доход
    print("Средний доход сотрудников: ", average_income)