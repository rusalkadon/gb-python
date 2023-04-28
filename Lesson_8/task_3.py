# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
# работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
class NotNumberError(Exception):
    def __init__(self, value):
        message = f"Ошибка: {value} не является числом"
        super().__init__(message)


numbers_list = []
while True:
    user_input = input("Введите число: ")
    if user_input.lower() == "stop":
        break
    try:
        number = float(user_input)
        if number.is_integer():
            number = int(number)
        numbers_list.append(number)
    except ValueError:
        print(NotNumberError(user_input))
print(numbers_list)