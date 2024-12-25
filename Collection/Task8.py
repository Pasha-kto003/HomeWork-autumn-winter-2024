import string

#1 кондиционер
temp = int(input('Введите температуру: '))
if temp >= 20:
    print('OFF')
elif temp < 20:
    print('ON')

#2 Время года
month = int(input('Введите месяц: '))
if 9 <= month < 12:
    print('Осень')
elif 6 <= month < 9:
    print('Лето')
elif 3 <= month < 6:
    print('Весна')
elif 1 <= month < 3 or month == 12:
    print('Зима')

#3 Собачий возраст к человеческому
age = int(input('Возраст собаки: '))
if age == 1:
    print(10.5)
elif age == 2:
    print(21)
elif 2 < age < 23:
    print(21 + ((age-2)*4))
elif age > 22:
    print('Ошибка - слишком большой возраст')
elif age < 1:
    print('Ошибка - слишком маленький возраст')
else:
    print('Ошибка - не ввели значение')

#4 Деление на 6
number = int(input('Введите число: '))
sum_number = 0
for i in str(number):
    sum_number += int(i)
if sum_number % 3 == 0:
    if number % 2 == 0:
        print(number / 6)
else:
    print('Ошибка')

#5 Пароль
p = input("Введите пароль: ")
lower_cnt = 0
upper_cnt = 0
spec_sym = 0
spec_s = "!  # $ % & ' ( ) * + , - . / : ; < = > ? @ [  ] ^ _ ` { | } ~"

for i in range(0, len(p)):
    if p[i].islower() == True:
        lower_cnt += 1
    if p[i].isupper() == True:
        upper_cnt += 1
    if p[i] in spec_s:
        spec_sym += 1

if lower_cnt > 0 and upper_cnt > 0 and spec_sym > 0 and len(p) >= 8:
    print("Пароль подходит")
else:
    print("Пароль не подходит")


