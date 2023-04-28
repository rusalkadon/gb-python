# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real*other.real - self.imag*other.imag,
                             self.imag*other.real + self.real*other.imag)


a = ComplexNumber(2, 3)
b = ComplexNumber(-1, 2)
c = a + b
d = a * b
print(c.real, c.imag) # 1 5
print(d.real, d.imag)  # -8 1