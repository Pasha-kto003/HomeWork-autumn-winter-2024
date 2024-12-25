def vklad(a, n):
    #Мин. вклад
    min_vklad = 30000
    #Проверка на минимальный депозит
    if a < min_vklad:
        return "Недостаточно средств для осуществления депозита"
    #Базовый процент
    percent = 0
    #Прибавка
    if a >= 10000:
        percent += (a // 10000) * 0.003
        if percent >= 0.05:
            percent = 0.05
    #проценты от длительности
    if n <= 3:
        dop_percent = 0.03
    if 3 < n < 7:
        dop_percent = 0.05
    elif n > 6:
        dop_percent = 0.02
    #Все проценты
    total_percent = percent + dop_percent
    #Сумма вклада
    total_amount = a
    #Сложный процент
    for year in range(1,3):
        total_amount *= (1 + total_percent)
    profit = total_amount - a
    return profit

if __name__ == "__main__":
    try:
        a = int(input("Введите сумму вклада (в рублях): "))
        n = int(input("Введите срок вклада (в годах): "))
        profit = vklad(a, n)
        print(f"Сумма прибыли: {profit} рублей")
    except ValueError as ve:
        print(f"Ошибка: {ve}")