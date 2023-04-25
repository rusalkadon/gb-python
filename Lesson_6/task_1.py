# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
import time


class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self):
        while True:
            if self.__color == "red":
                print("Red light is on")
                time.sleep(7)
                self.__color = "yellow"
            elif self.__color == "yellow":
                print("Yellow light is on")
                time.sleep(2)
                self.__color = "green"
            elif self.__color == "green":
                print("Green light is on")
                time.sleep(5)
                self.__color = "red"


tl = TrafficLight()
tl.running()
