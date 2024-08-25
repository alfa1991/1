def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Первая цифра числа
        first = int(str_number[0])
        # Рекурсивный вызов функции для оставшейся части числа
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки 1 или меньше, возвращаем эту цифру
        return int(str_number)


# Пример использования функции
print(get_multiplied_digits(40203))  # Вывод: 0, так как произведение цифр включает 0