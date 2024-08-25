# Глобальная переменная для подсчета вызовов функций
calls = 0

# Функция для увеличения счетчика вызовов
def count_calls():
    global calls
    calls += 1

# Функция для обработки строки и возвращения необходимой информации
def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    return (len(string), string.upper(), string.lower())

# Функция для проверки, содержится ли строка в списке (без учета регистра)
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower

# Тестируем функции с примерными данными
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

# Выводим общее количество вызовов
print(calls)
