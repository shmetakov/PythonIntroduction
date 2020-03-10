class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Машина: {name}, цвет: {color}, полиейская: {is_police}")

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, dir):
        print(f"{self.name} повернула {'налево' if dir else 'направо'}")

    def show_speed(self):
        print(f"{self.name} скорость: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"{self.name} скорость: {self.speed if self.speed <= 60 else 'превышение скорости'}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"{self.name} скорость: {self.speed if self.speed <= 40 else 'превышение скорости'}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(60, "белая", "Городская машина")
town_car.go()
town_car.turn(1)
town_car.turn(0)
town_car.stop()
town_car.show_speed()
print()

sport_car = SportCar(160, "черная", "Спортивная машина")
sport_car.go()
sport_car.turn(1)
sport_car.turn(0)
sport_car.stop()
sport_car.show_speed()
print()

work_car = WorkCar(60, "желтая", "Рабочая машина")
work_car.go()
work_car.turn(1)
work_car.turn(0)
work_car.stop()
work_car.show_speed()
print()

police_car = PoliceCar(90, "синяя", "Полицеская машина")
police_car.go()
police_car.turn(1)
police_car.turn(0)
police_car.stop()
police_car.show_speed()
print()
