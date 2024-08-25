def get_matrix(n, m, value):
    # Создание пустого списка для матрицы
    matrix = []

    # Внешний цикл для строк
    for i in range(n):
        # Создание пустой строки
        row = []

        # Внутренний цикл для столбцов
        for j in range(m):
            # Добавление значения value в строку
            row.append(value)

        # Добавление строки в матрицу
        matrix.append(row)

    return matrix


# Пример вызова функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результата на консоль
print(result1)
print(result2)
print(result3)