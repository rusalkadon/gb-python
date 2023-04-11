# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
def print_user_info(name, surname, birth_year, city, email, phone):
    print(f"User: {name} {surname}, born in {birth_year}, lives in {city}, email: {email}, phone: {phone}")
