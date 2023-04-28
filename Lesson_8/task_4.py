# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
class Warehouse:
    def __init__(self, location):
        self.location = location
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)


class OfficeEquipment:
    def __init__(self, brand, model, price, weight):
        self.brand = brand
        self.model = model
        self.price = price
        self.weight = weight


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, weight, is_color):
        super().init(brand, model, price, weight)
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, weight, resolution):
        super().init(brand, model, price, weight)
        self.resolution = resolution


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, price, weight, max_pages_per_minute):
        super().init(brand, model, price, weight)
        self.max_pages_per_minute = max_pages_per_minute
