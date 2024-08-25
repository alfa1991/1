def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру для корректного сравнения
    root_word_lower = root_word.lower()
    # Создаем пустой список для хранения слов с общим корнем
    same_words = []

    # Перебираем все слова в other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру для сравнения
        word_lower = word.lower()
        # Проверяем, содержится ли root_word в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Возвращаем сформированный список
    return same_words


# Примеры вызова функции и вывод результата на консоль
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)  # Ожидаемый результат: ['richiest', 'orichalcum', 'richies']
print(result2)  # Ожидаемый результат: ['Able', 'Disable']
