# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Используйте написанную ранее функцию int_func().
def int_func(word):
    return word.capitalize()


input_str = input("Введите строку из слов, разделенных пробелом: ")

words = input_str.split()
capitalized_words = map(int_func, words)
output_str = " ".join(capitalized_words)

print(output_str)
