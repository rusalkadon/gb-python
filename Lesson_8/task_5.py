# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру (например, словарь).
class Warehouse:
    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def receive(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def transfer(self, item, quantity, department):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            department.receive(item, quantity)
            print(f"{quantity} {item} transferred to {department.name}")
        else:
            print("Not enough inventory to transfer")

class OfficeEquipment:
    def __init__(self, model, price):
        self.model = model
        self.price = price

class Printer(OfficeEquipment):
    def __init__(self, model, price, printing_technology):
        super().__init__(model, price)
        self.printing_technology = printing_technology

class Scanner(OfficeEquipment):
    def __init__(self, model, price, scan_resolution):
        super().__init__(model, price)
        self.scan_resolution = scan_resolution

class Copier(OfficeEquipment):
    def __init__(self, model, price, copy_speed):
        super().__init__(model, price)
        self.copy_speed = copy_speed

class Department:
    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def receive(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

warehouse = Warehouse("Main Warehouse")
marketing = Department("Marketing Department")
finance = Department("Finance Department")

printer = Printer("HP LaserJet", 250, "Laser")
scanner = Scanner("Epson", 150, "6400 x 9600 dpi")
copier = Copier("Canon", 1000, "105 ppm")

warehouse.receive(printer.model, 10)
warehouse.receive(scanner.model, 5)
warehouse.receive(copier.model, 3)

warehouse.transfer(printer.model, 3, marketing)
warehouse.transfer(scanner.model, 2, finance)