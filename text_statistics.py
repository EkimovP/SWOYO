import re


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def text_stat(filename):
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            text = file.readlines()
    except FileNotFoundError:
        return {'error': 'Файл не найден'}
    except Exception as e:
        return {'error': str(e)}
    final_dictionary = {}
    # Количество слов в тексте
    list_of_words_text = []
    for i in range(len(text)):
        # Учитываем только буквы латинского или кириллического алфавита
        list_of_words_text += re.findall(r'\b[A-Za-zА-Яа-я]+', text[i])
    final_dictionary['word_amount'] = len(list_of_words_text)

    # Количество абзацев в тексте
    count_paragraph = 0
    for i in range(len(text)):
        # Если строка является переводом на следующую строку
        if text[i] == '\n':
            continue
        # Если строка не пустая
        if len(text[i]) != 0:
            count_paragraph += 1
    final_dictionary['paragraph_amount'] = count_paragraph
    
    # Создаем словарь для хранения результатов частоты использования букв и доли слов с буквой
    result_dict = {}
    # Создаем множество всех букв русского и английского алфавитов
    all_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'
    for i in range(len(list_of_words_text)):
        list_of_words_text[i] = list_of_words_text[i].lower()
    # Список состоящий из буквы латинского или кириллического алфавита, имеющих только нижний регистр
    list_cyrillic_and_latin = [i.lower() for i in list(''.join(text)) if i.lower() in all_letters]
    # Всего букв
    all_quantity = 0
    for i in list_cyrillic_and_latin:
        all_quantity += 1
    # Подсчитываем частоту использования и долю слов для каждой буквы
    for letter in all_letters:
        letter_count = 0
        words_with_letter = 0
        for word in list_of_words_text:
            if letter in word:
                letter_count += word.count(letter)
                words_with_letter += 1
        # Доля слов для конкретной буквы
        percentage_words_with_letter = words_with_letter / len(list_of_words_text)
        if percentage_words_with_letter != 0:
            percentage_words_with_letter = toFixed(percentage_words_with_letter, 5)
        # Частота использования каждой буквы латинского или кириллического алфавита
        letter_frequency = letter_count / all_quantity
        if letter_frequency != 0:
            letter_frequency = toFixed(letter_frequency, 5)
        result_dict[letter] = (letter_frequency, percentage_words_with_letter)
    final_dictionary.update(result_dict)
    
    # Количество слов, в которых одновременно встречаются буквы обоих алфавитов
    alphabet_cyrillic = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    alphabet_latin = set('abcdefghijklmnopqrstuvwxyz')
    # Счетчик слов, в которых встречаются буквы обоих алфавитов
    words_with_both_alphabets_count = 0
    # Перебираем слова
    for word in list_of_words_text:
        contains_latin = any(letter in alphabet_latin for letter in word)
        contains_cyrillic = any(letter in alphabet_cyrillic for letter in word)
        if contains_latin and contains_cyrillic:
            words_with_both_alphabets_count += 1
    final_dictionary['bilingual_word_amount'] = words_with_both_alphabets_count
    return final_dictionary