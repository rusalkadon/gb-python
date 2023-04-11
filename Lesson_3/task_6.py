# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func(word):
    """
    Принимает слово из маленьких латинских букв и возвращает его же,
    но с прописной первой буквой.
    """
    return word.capitalize()

# Пример использования функции:
print(int_func('text')) # Output: Text