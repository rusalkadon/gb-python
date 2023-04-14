# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). Она отвечает за
# получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial


for el in fact(5):
    print(el)
