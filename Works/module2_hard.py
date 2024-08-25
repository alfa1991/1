def generate_password(n):
    pairs = []
    result = ""

    # Перебираем все возможные пары чисел от 1 до n-1
    for i in range(1, n):
        for j in range(i + 1, n):
            if (i + j) % n == 0:
                pairs.append((i, j))

    # Формируем строку из пар
    for pair in pairs:
        result += str(pair[0]) + str(pair[1])

    return result

# Ввод числа
n = int(input("Введите число (от 3 до 20): "))

# Генерация и вывод пароля
password = generate_password(n)
print("Нужный пароль:", password)

# Функция generate_password:
# Принимает число n.
# Инициализирует пустой список pairs и пустую строку result.
# Генерация пар:
# Внешний цикл for i in range(1, n) перебирает значения от 1 до n-1.
# Внутренний цикл for j in range(i + 1, n) перебирает значения от i+1 до n-1.
# Проверяем, кратна ли сумма пары числу n ((i + j) % n == 0).
# Если условие выполняется, добавляем пару в список pairs.
# Формирование пароля:
# Преобразуем список пар в строку, добавляя каждую пару в result.
# Ввод и вывод:
# Вводим значение n от пользователя.
# Вызываем функцию generate_password и выводим результат.