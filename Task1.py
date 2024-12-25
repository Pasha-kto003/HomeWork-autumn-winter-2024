
def f(value,fromU,toU):
    units = {"сек": 1, "мин": 60, "час": 3600}
    value_in_sec = int(value) * units[fromU]
    converted_value = value_in_sec / units[toU]
    return converted_value


value = input("Введите значение времени: ")
fromU = input("Введите исходную единицу времени (сек мин час): ")
toU = input("Введите выводимую единицу времени (сек мин час): ")
res = f(value,fromU,toU)
print(f"{value} {fromU} = {res} {toU}")