def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()  # Вызов inner_function внутри test_function

# Вызываем test_function, чтобы выполнить и inner_function
test_function()

# Попытка вызвать inner_function вне test_function вызовет ошибку,
# так как inner_function определена только в области видимости test_function.
# Следующий вызов приведет к ошибке и поэтому закомментирован:
# inner_function()  # Раскомментируйте эту строку, чтобы увидеть ошибку выполнения.