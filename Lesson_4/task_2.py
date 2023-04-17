# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
def greater_than_previous(numbers):
    res = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
    return res


numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res = greater_than_previous(numbers)
print(res)  # [12, 44, 4, 10, 78, 123]
