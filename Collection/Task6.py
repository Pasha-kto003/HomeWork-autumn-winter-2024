# Сборник заданий по лабароторной работе
#1
a = int(9)
b = float(6.66)
c = str('абвгде')
d = True
e = False
print(a,b,c,d,e)

#2
Name = input('Введите имя: ')
Vozrast = input('Введите возраст: ')
print(Name, Vozrast)

#3
q = 342
w = float(56.2)
e = 43
r = q+w+e
print(r)

#4
a = 3
b = 8
c = (a + 4*b)*(a - 3*b) + a**2
print(c)

#5
a = int(input('Длина'))
b = int(input('Ширина'))
pl = a*b
per = 2*a + 2*b
print(pl,per)

#6
print('*   *   *')
print(' * * * *')
print('  *   *')

#7
a = 6
b = 8
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b, a<b, a>b, a<=b, a==b, a!=b, a >= b)

#8
x1 = str('Семен')
x2 = 18
print(f'Меня зовут {x1}, мне {x2} лет')

#9
a = "Съешь ещё "
b = "этих "
c = "мягких французских булок"
d = ", "
e = "да выпей ч"
f = "аю"
print(a + b + c + d + e + f)

#10
a = "Нет! Да! "
print(a*4)

#11
a = int(input("Первое число"))
b = int(input("Второе число"))
c = int(input("Третье число"))
d = (a + b) // c
print(f'Результат вычисления: {d}')

#12
a = input("Введите ваше слово:")
print(a[:4])
print(a[-2:])
print(a[3:8])
print(a[::-1])