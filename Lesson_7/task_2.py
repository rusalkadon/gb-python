# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothing(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass

class Coat(Clothing):
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)

class Suit(Clothing):
    def __init__(self, height):
        self._height = height

    @property
    def height(self):
        return self._height

    def fabric_consumption(self):
        return round(2 * self.height + 0.3, 2)

coat = Coat(46)
suit = Suit(170)

print(f"Расход ткани на пальто размера {coat.size}: {coat.fabric_consumption()} метров.")
print(f"Расход ткани на костюм роста {suit.height}: {suit.fabric_consumption()} метров.")