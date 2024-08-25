class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    # Перегрузка метода для сравнения объектов класса Building
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


# Пример использования
building1 = Building(10, 'office')
building2 = Building(10, 'office')
building3 = Building(5, 'residential')

print(building1 == building2)  # Выведет True, поскольку атрибуты объектов совпадают
print(building1 == building3)  # Выведет False, так как атрибуты объектов различаются