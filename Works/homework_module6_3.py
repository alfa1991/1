class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000

    def horse_powers(self):
        return 0

class Nissan(Vehicle, Car):
    def __init__(self, price, vehicle_type):
        self.price = price
        self.vehicle_type = vehicle_type

    def horse_powers(self):
        return 300

# Создаем экземпляр класса Nissan
nissan_car = Nissan(price=1500000, vehicle_type="sedan")

# Распечатываем свойства vehicle_type и price
print(f"Тип транспорта: {nissan_car.vehicle_type}")
print(f"Цена: {nissan_car.price}")
