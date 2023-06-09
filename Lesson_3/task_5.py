# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых
# чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.
def sum_numbers():
    total_sum = 0

    while True:
        if total_sum != 0:
            print(f"Общая сумма: {total_sum}")

        user_input = input("Введите числа, разделенные пробелом, или 'q' для выхода: ")

        if user_input.lower() == 'q':
            break

        numbers = user_input.split()

        try:
            numbers = [int(num) for num in numbers]
            total_sum += sum(numbers)
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")
            continue

    print(f"Общая сумма: {total_sum}")


sum_numbers()
