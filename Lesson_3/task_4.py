# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа x
# в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора .
# Второй — более сложная реализация без оператора , предусматривающая использование цикла.

def my_func(x, y):
    if y == 0:
        return 1
    result = 1
    for i in range(abs(y)):
        result *= x
    if y < 0:
        return 1 / result
    return result
