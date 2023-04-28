# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.
class DivisionByZeroError(Exception):
    def __init__(self):
        self.message = "Деление на ноль запрещено"
        super().__init__(self.message)

def divide_numbers(a, b):
    if b == 0:
        raise DivisionByZeroError
    return a / b


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    result = divide_numbers(a, b)
    print(f"Результат деления: {result}")
except DivisionByZeroError as e:
    print(e.message)