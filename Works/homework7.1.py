# Создание словаря
my_dict = {"Иван": 1990, "Анна": 1992, "Сергей": 1985}

# Выводим на экран словарь my_dict
print(my_dict)

# Выводим значение по существующему ключу
print(my_dict.get("Иван"))

# Выводим значение по отсутствующему ключу
print(my_dict.get("Алексей", "Ключ не найден"))

# Добавляем новые пары
my_dict["Мария"] = 1995
my_dict["Дмитрий"] = 1988

# Удаляем одну пару и выводим значение
удалённое_значение = my_dict.pop("Анна")
print(удалённое_значение)

# Выводим на экран обновленный словарь my_dict
print(my_dict)
