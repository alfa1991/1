# Дан список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создайте пустые списки primes и not_primes
primes = []
not_primes = []

# Перебираем список numbers
for number in numbers:
    # Отметить простоту числа можно переменной is_prime
    is_prime = True

    # Проверяем число на простоту
    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    # В зависимости от значения is_prime добавляем число в соответствующий список
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Выводим списки primes и not_primes на экран
print("Простые числа:", primes)
print("Не простые числа:", not_primes)