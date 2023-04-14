# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные
# числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
import functools
import operator

even_numbers = [num for num in range(100, 1001, 2)]
result = functools.reduce(operator.mul, even_numbers)
print(result)