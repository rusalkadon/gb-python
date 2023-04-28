 # Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        return cls(day, month, year)

    @staticmethod
    def validate(day, month, year):
        if not 1 <= month <= 12:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if day > 29:
                    return False
            else:
                if day > 28:
                    return False
        else:
            if day > 31:
                return False
        return True

# Пример:
date_string = '27-04-2023'
day, month, year = map(int, date_string.split('-'))
if Date.validate(day, month, year):
    date = Date.from_string(date_string)
    print(date.day, date.month, date.year)
else:
    print('Invalid date')