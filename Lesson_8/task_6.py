# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
class Warehouse:
    def __init__(self):
        self.inventory = {} # словарь для хранения оргтехники и их количества

    def add_item(self, item):
        if isinstance(item, OfficeEquipment):
            if item.name not in self.inventory:
                self.inventory[item.name] = {'count': 0, 'items': []}
            self.inventory[item.name]['count'] += 1
            self.inventory[item.name]['items'].append(item)
            print(f"{item.name} added to the warehouse.")
        else:
            print("Invalid item type.")

    def move_item(self, equipment, department):
        item_name = equipment.name
        if item_name not in self.inventory:
            print(f"{item_name} is not in the warehouse.")
            return
        if self.inventory[item_name]['count'] == 0:
            print(f"No {item_name} in the warehouse.")
            return
        if department.name not in Department.departments:
            print(f"{department.name} department does not exist.")
            return
        item = self.inventory[item_name]['items'].pop()
        self.inventory[item_name]['count'] -= 1
        department.add_item(item)
        print(f"{item_name} moved to {department.name} department.")

    def print_items(self):
        print(self.inventory)

class OfficeEquipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def str(self):
        return f"{self.name} ({self.price}$)"

class Printer(OfficeEquipment):
    def __init__(self, name, price, print_speed):
        super().__init__(name, price)
        self.print_speed = print_speed

class Scanner(OfficeEquipment):
    def __init__(self, name, price, scan_quality):
        super().__init__(name, price)
        self.scan_quality = scan_quality

class Xerox(OfficeEquipment):
    def __init__(self, name, price, copy_speed):
        super().__init__(name, price)
        self.copy_speed = copy_speed

class Department:
    departments = ['sales', 'marketing', 'hr', 'it']

    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def add_item(self, item):
        if isinstance(item, OfficeEquipment):
            if item.name not in self.inventory:
                self.inventory[item.name] = {'count': 0, 'items': []}
            self.inventory[item.name]['count'] += 1
            self.inventory[item.name]['items'].append(item)
            print(f"{item.name} added to the {self.name} department.")
        else:
            print("Invalid item type.")

    def print_items(self):
        print(self.inventory)

# создаем склад и отделы компании
warehouse = Warehouse()
sales = Department('sales')
marketing = Department('marketing')
hr = Department('hr')
it = Department('it')

# добавляем на склад оргтехнику
printer1 = Printer('HP LaserJet', 300, '20 pages per minute')
printer2 = Printer('Canon', 150, '10 pages per minute')
scanner1 = Scanner('Epson', 200, '2400 dpi')
xerox1 = Xerox('Xerox', 500, '25 pages per minute')
warehouse.add_item(printer1)
warehouse.add_item(printer2)
warehouse.add_item(scanner1)
warehouse.add_item(xerox1)

# перемещаем оргтехнику в отделы
warehouse.move_item(printer1, sales)
warehouse.move_item(printer2, marketing)
warehouse.move_item(scanner1, it)
warehouse.move_item(xerox1, hr)

# выводим информацию о наличии оргтехники на складе и в отделах
warehouse.print_items()
sales.print_items()
marketing.print_items()
it.print_items()
hr.print_items()