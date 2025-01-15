def sample_numbers(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sample_numbers_range(start, end):
    if not (isinstance(start, int) and isinstance(end, int)):
        return "Ошибка"
    if (start > end) or (start < 0 or end < 0):
        return "Ошибка"

    primes = []
    for number in range(start, end + 1):
        if sample_numbers(number):
            primes.append(number)
    return primes


start_input = input("Введите начало диапазона: ")
end_input = input("Введите конец диапазона: ")
start = int(start_input)
end = int(end_input)
result = sample_numbers_range(start, end)
print("Простые числа в диапазоне {}: {}".format((start, end), result))
