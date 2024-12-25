def vklad(a, n):
    # Проверка на минимальный вклад
    if a < 30000:
        return "Мало"
    
    # Базовый процент с ограничением
    procent = min((a // 10000) * 0.003, 0.05) if a >= 10000 else 0

    # Дополнительный процент в зависимости от срока вклада
    dop_procent = 0.03 if n <= 3 else 0.05 if 3 < n < 7 else 0.02

    # Общий процент
    total_procent = procent + dop_procent

    # Расчёт сложных процентов
    total_amount = a * ((1 + total_procent) ** n)
    profit = total_amount - a
    return profit

if __name__ == "__main__":
    try:
        a = int(input("Введите сумму вклада (в рублях): "))
        n = int(input("Введите срок вклада (в годах): "))
        result = vklad(a, n)
        print(f"Сумма прибыли: {result:.2f} рублей" if isinstance(result, (int, float)) else result)
    except ValueError as ve:
        print(f"Ошибка ввода: {ve}")
