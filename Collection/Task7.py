#1
a = input('Имя: ')
b = input('Возраст: ')
s = 0
while s < 10:
    s = s+1
    print(f"Меня зовут {a} и мне {b} лет")
print('\n')

#2
a = input('Число (таблица умножения) : ')
b = 0
while b < 10:
    b = b + 1
    print(int(a)*b)
print('\n')

#3
a = 0
while a < 99:
    a = a+3
    print(a)
print('\n')

#4
a = int(input("Число факториал: "))
for b in range(1,int(a)):
    a = a*b
print(a)
print('\n')

#5
a = 21
while a > 0:
    a = a-1
    print(a)
print('\n')

#6
fib1 = fib2 = 1
n = int(input('Число фибоначчи '))
print(fib1, fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
print('\n')

#7
INPUT = input('Слово: ')
c = 1
for INPUTS in INPUT:
    print(f'{INPUTS}{c}', end='')
    c = c+1
print('\n')

#8
a = 9999999
while a > 0:
    input1 = int(input('Первое число '))
    input2 = int(input('Первое число '))
    print(input1+input2)
    a = a - 1