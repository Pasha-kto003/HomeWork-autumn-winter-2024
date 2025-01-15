def vklad(money, years):
    min_vklad = 30000
    if money < min_vklad:
        return "Недостаточно средств для осуществления вклада"
    percent = 0
    if money >= 10000:
        percent += (money // 10000) * 0.003
        if percent >= 0.05:
            percent = 0.05
    if years <= 3:
        dop_percent = 0.03
        print(f'Ваш доп. процент по вкладу: {dop_percent}')
    if 3 < years < 7:
        dop_percent = 0.05
        print(f'Ваш доп. процент по вкладу: {dop_percent}')
    elif years > 6:
        dop_percent = 0.02
        print(f'Ваш доп. процент по вкладу: {dop_percent}')
    total_percent = percent + dop_percent
    total_amount = money
    for year in range(1, 3):
        total_amount *= (1 + total_percent)
    message = total_amount - money
    return message


if __name__ == "__main__":
    try:
        money = int(input("Введите сумму вклада (в рублях): "))
        years = int(input("Введите срок вклада (в годах): "))
        profit = vklad(money, years)
        print(f"Сумма прибыли: {profit} рублей")
    except ValueError as ve:
        print(f"Ошибка: {ve}")