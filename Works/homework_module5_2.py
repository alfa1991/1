class House:
    def __init__(self):
        # Изначально количество этажей равно 0
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        # Изменение количества этажей на заданное значение
        self.numberOfFloors = floors
        # Вывод измененного значения в консоль
        print(self.numberOfFloors)

# Создание экземпляра класса House
my_house = House()

# Изменение количества этажей дома и вывод результата в консоль
my_house.setNewNumberOfFloors(6)