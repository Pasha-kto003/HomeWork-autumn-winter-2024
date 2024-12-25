def is_prime(num):
    """Проверка на простое число."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """Поиск простых чисел в заданном диапазоне."""
    if not (isinstance(start, int) and isinstance(end, int)) or start < 0 or end < 0:
        return "Ошибка: Диапазон должен быть неотрицательными числами."
    if start > end:
        return "Ошибка: Начало диапазона больше конца."

    return [num for num in range(start, end + 1) if is_prime(num)]

if __name__ == "__main__":
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
        result = primes_in_range(start, end)
        if isinstance(result, str):
            print(result)  # Вывод сообщения об ошибке
        else:
            print(f"Простые числа в диапазоне ({start}, {end}): {result}")
    except ValueError:
        print("Ошибка: Введите целые числа.")
