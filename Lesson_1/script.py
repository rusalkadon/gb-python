# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
# Пример работы с переменными и вводом данных:
# python
# создание переменных
name = "Mary"
age = 20
height = 1.70

# вывод на экран
print(f"Меня зовут  {name}, Мне  {age}  лет, Мой рост  {height}")

# запрос числа у пользователя и сохранение в переменную
number = int(input("Введите число: "))
print("Вы ввели число", number)

# запрос строки у пользователя и сохранение в переменную
string = input("Введите строку: ")
print("Вы ввели строку", string)
# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
time_in_seconds = int(input("Введите время в секундах: "))

# вычисление часов, минут и секунд
hours = time_in_seconds // 3600
minutes = (time_in_seconds % 3600) // 60
seconds = time_in_seconds % 60

# вывод времени в формате чч:мм:сс
print(f"{hours:02}:{minutes:02}:{seconds:02}")

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
n = int(input("Введите число: "))

# вычисление суммы
nn = n * 11
nnn = n * 111
sum = n + nn + nnn

# вывод результата
print(f"Сумма чисел {n} + {nn} + {nnn} = {sum}")
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции./
# запрос числа у пользователя и сохранение в переменную
number = int(input("Введите число: "))

# поиск наибольшей цифры
max_digit = 0
while number > 0:
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
    number //= 10

# вывод результата
print("Наибольшая цифра в числе:", max_digit)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
revenue = float(input("Введите значение выручки: "))
expenses = float(input("Введите значение издержек: "))

# вычисление прибыли/убытка
profit = revenue - expenses

# вывод результата
if profit > 0:
    print("Фирма работает с прибылью")
elif profit < 0:
    print("Фирма работает с убытком")
else:
    print("Фирма работает в ноль")
# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
revenue = float(input("Введите значение выручки: "))
costs = float(input("Введите значение издержек: "))

if revenue > costs:
    profit = revenue - costs
    print("Фирма работает с прибылью. Прибыль составляет: ", profit)
    profitability = profit / revenue
    print("Рентабельность выручки составляет: ", profitability)
    num_employees = int(input("Введите численность сотрудников: "))
    profit_per_employee = profit / num_employees
    print("Прибыль в расчёте на одного сотрудника составляет: ", profit_per_employee)
elif revenue == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает с убытком")
# 7.py. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
a = float(input("Введите результат спортсмена в первый день, в км: "))
b = float(input("Введите желаемый результат спортсмена, в км: "))

distance = a
day = 1

while distance < b:
    print(f"{day}-й день: {distance:.2f} км")
    distance *= 1.1
    day += 1

print(f"{day}-й день: {distance:.2f} км")
print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.")

