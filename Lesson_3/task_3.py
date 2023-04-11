# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших
# двух аргументов.
def my_func(a, b, c):
    numbers = [a, b, c]
    return sum(numbers) - min(numbers)
