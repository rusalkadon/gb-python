# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.Создайте экземпляры классов, передайте значения
# атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color} {self.name} is moving")

    def stop(self):
        print(f"{self.color} {self.name} has stopped")

    def turn(self, direction):
        print(f"{self.color} {self.name} turned {direction}")

    def show_speed(self):
        print(f"{self.color} {self.name} speed is {self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Warning! Speed limit exceeded.")
        super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Warning! Speed limit exceeded.")
        super().show_speed()


class PoliceCar(Car):
    def init(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


town_car = TownCar(70, "white", "Nissan")
sport_car = SportCar(120, "red", "Ferrari")
work_car = WorkCar(50, "black", "VW")
police_car = PoliceCar(80, "blue", "Ford")

town_car.go()
town_car.turn("right")
town_car.show_speed()

sport_car.go()
sport_car.turn("left")
sport_car.show_speed()

work_car.go()
work_car.stop()
work_car.show_speed()

police_car.go()
police_car.turn("left")
police_car.show_speed()
