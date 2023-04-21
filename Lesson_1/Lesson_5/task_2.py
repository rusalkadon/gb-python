# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.
filename: str = 'task_2.txt'  # название файла

with open(filename, 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        words = line.split()  # разбиваем строку на слова
        print(f"Строка {i + 1} содержит {len(words)} слов")

    print(f"В файле всего {len(lines)} строк")
