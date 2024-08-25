class Building:
    total = 0  # Атрибут класса, отслеживающий количество объектов

    def __init__(self):
        Building.total += 1  # Увеличиваем счетчик при создании нового объекта

# Создаем 40 объектов класса Building
buildings = [Building() for _ in range(40)]

# Выводим на экран количество созданных объектов
print(f"Создано {Building.total} объектов класса Building")
