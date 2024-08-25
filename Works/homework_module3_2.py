def print_params(a=1, b='строка', c=True):
    print(f'a = {a}, b = {b}, c = {c}')


# Вызов функции с разным количеством аргументов
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(5, 'текст', False)

# Создание списка с тремя элементами разных типов
values_list = [10, 'example', False]

# Создание словаря с тремя ключами, соответствующими параметрам функции print_params и значениями разных типов
values_dict = {'a': 99, 'b': 'dictionary', 'c': [3, 4, 5]}

# Передача списка и словаря в функцию print_params с помощью распаковки
print_params(*values_list)
print_params(**values_dict)

# Создание списка с двумя элементами разных типов
values_list_2 = [54.32, 'Строка']

# Вызов функции с использованием распаковки списка и добавлением отдельного параметра
print_params(*values_list_2, 42)
