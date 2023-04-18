# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить её на экран.
with open("task_5.txt", "w", encoding='utf-8') as file:
    # генерируем список чисел
    numbers = list(range(1, 30, 3))
    # преобразуем список в строку, разделяя числа пробелами
    numbers_str = " ".join(map(str, numbers))
    # записываем строку в файл
    file.write(numbers_str)

# открываем файл для чтения
with open("task_5.txt", "r", encoding='utf-8') as file:
    # считываем содержимое файла
    content = file.read()
    # преобразуем содержимое файла в список чисел
    numbers_list = list(map(int, content.split()))
    # вычисляем сумму чисел в списке
    sum_numbers = sum(numbers_list)
    # выводим результат на экран
    print("Сумма чисел в файле:", sum_numbers)
