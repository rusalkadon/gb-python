# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее. Подсказка: используйте функцию count() и
# cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие
# его завершения. #### Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем
# цикл. Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle


def num_generator(start, stop):
    for num in count(start):
        if num > stop:
            break
        yield num


# Создаем итератор, повторяющий элементы некоторого списка, определённого заранее
def list_repeater(lst, stop):
    counter = 0
    for elem in cycle(lst):
        if counter > stop:
            break
        yield elem
        counter += 1


# Пример использования функций
gen = num_generator(3, 10)
for num in gen:
    print(num)

lst = ['a', 'b', 'c']
repeater = list_repeater(lst, 5)
for elem in repeater:
    print(elem)
