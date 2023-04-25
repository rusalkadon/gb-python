# 5.Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером {self.title}")


pen = Pen("Parker")
pencil = Pencil("Faber-Castell")
handle = Handle("Stabilo")

pen.draw()
pencil.draw()
handle.draw()