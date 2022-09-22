# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвёртое число: '))
e = int(input('Введите пятое число: '))
max = 0
if a > b:
    max = a
elif b > a:
    max = b
elif c > max:
    max = c
else:
    max = max
if d > max:
    max = d
else:
    max = max
if e > max:
    max = e
else:
    max = max
print(max)
