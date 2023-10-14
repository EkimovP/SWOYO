from text_statistics import text_stat


def test_file_not_found():
    filename = "несуществующий_файл.txt"
    result = text_stat(filename)
    assert result == {'error': 'Файл не найден'}


def test_analyze_text():
    # Необходимо указать путь к файлу
    result = text_stat("D:/Python_project/SWOYO/text_for_the_test.txt")
    # Проверка количества абзацев
    assert 'paragraph_amount' in result
    assert result['paragraph_amount'] == 2
    # Проверка количества слов
    assert 'word_amount' in result
    assert result['word_amount'] == 6
    # Проверка частоты использования буквы 'а'
    assert 'а' in result
    assert result['а'][0] == '0.18182'
    # Проверка доли слов с буквой 'а'
    assert result['а'][1] == '0.50000'
    # Проверка количества слов с использованием букв из обоих алфавитов
    assert 'bilingual_word_amount' in result
    assert result['bilingual_word_amount'] == 1