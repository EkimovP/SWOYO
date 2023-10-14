def prime_numbers(low, high):
    list_prime_numbers = []
    # Проверка параметров функции на тип данных
    if not (isinstance(low, int) and isinstance(high, int)):
        return list_prime_numbers
    # Если верхняя граница диапазона меньше либо равна единице
    elif high <= 1:
        return list_prime_numbers
    # Если нижняя граница диапазона меньше либо равна единице
    elif low <= 1:
        low = 2
    # Алгоритм нахождения простых чисел (решето Эратосфена)
    is_prime = [True] * (high + 1)
    p = 2
    while (p * p <= high):
        # Проверка: является ли p простым числом
        if is_prime[p]:
            for i in range(p * p, high + 1, p):
                is_prime[i] = False
        p += 1
    # Записываем простые числа в список
    list_prime_numbers = [num for num, prime in enumerate(is_prime) if prime and num >= low]
    # Выводим отсортированный по возрастанию список простых чисел, если они есть в заданном диапазоне, иначе пустой список
    return list_prime_numbers