# Листинг 1: Программа без функции для вычисления корня уравнения x^2 - 4 = 0 (метод деления пополам)
from math import *
a = -10
b = 10
while (b - a) > 10 ** (-10):
    c = (a + b) / 2
    f_a = a ** 2 - 4
    f_b = b ** 2 - 4
    f_c = c ** 2 - 4
    if f_a * f_c > 0:
        a = c
    else:
        b = c
print((a + b) / 2)

# Листинг 2: Функция funkcija(x) для уравнения x^2 + 4x + 4 и метод деления пополам
from math import *
def funkcija(x):
    f = x ** 2 + 4 * x + 4
    return f
a = -10
b = 10
while (b - a) > 10 ** (-10):
    c = (a + b) / 2
    f_a = funkcija(a)
    f_b = funkcija(b)
    f_c = funkcija(c)
    if f_a * f_c > 0:
        a = c
    else:
        b = c
print((a + b) / 2)

# Листинг 3: Функция function(x) и функция Bisection(a, b, e) для уравнения x^2 - 4 = 0
from math import *
def function(x):
    f = x ** 2 - 4
    return f
def Bisection(a, b, e):
    while (b - a) > e:
        c = (a + b) / 2
        f_a = function(a)
        f_b = function(b)
        f_c = function(c)
        if f_a * f_c > 0:
            a = c
        else:
            b = c
    return ((a + b) / 2)
A = -10
B = 10
E = 10 ** (-15)
print(Bisection(A, B, E))

# Листинг 4: Функция Bisection, возвращающая кортеж (корень, количество шагов)
from math import *
def function(x):
    f = x ** 2 - 4
    return f
def Bisection(a, b, e):
    n = 0
    while (b - a) > e:
        n = n + 1
        c = (a + b) / 2
        f_a = function(a)
        f_b = function(b)
        f_c = function(c)
        if f_a * f_c > 0:
            a = c
        else:
            b = c
    return ((a + b) / 2, n)
A = -10
B = 10
E = 10 ** (-15)
print(Bisection(A, B, E))

# Листинг 5: Пример обязательных аргументов (функция summa)
def summa(a, b):
    c = a + b
    return c
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
summa(num1, num2)

# Листинг 6: Функция Degree с необязательным параметром (по умолчанию a=2)
def Degree(x, a=2):
    f = x ** a
    return f
print(Degree(3))      # возведение в квадрат
print(Degree(3, 4))   # возведение в четвёртую степень

# Листинг 7: Функция Clothing с именованными аргументами
def Clothing(Dress, ColorDress, Shoes, ColorShoes):
    S = 'Сегодня я надену ' + ColorDress + ' ' \
        + Dress + ' и ' + ColorShoes + ' ' + Shoes
    return S
print(Clothing(ColorDress='красное', Dress='платье', ColorShoes='чёрные', Shoes='туфли'))

# Листинг 8: Функция с произвольным количеством аргументов (*args)
def unknown(*args):
    for argument in args:
        print(argument)
unknown('Что ', 'происходит', '?')
unknown('Не знаю!')

# Листинг 9: Примеры локальных и глобальных переменных
# 9.1 Функция mathem (передача копий значений)
def mathem(a, b):
    a = a / 2
    b = b + 10
    print(a + b)
num1 = 100
num2 = 12
mathem(num1, num2)
print(num1)
print(num2)
# (попытка обратиться к a или b вызовет ошибку, закомментировано)
# print(a)  # NameError

# 9.2 Функция mathem2 (доступ к глобальным переменным)
def mathem2():
    print(num1 + num2)
mathem2()

# 9.3 Глобальная и локальная переменная Place
Place = 'Солнечная система'   # Глобальная переменная
def global_Position():
    print(Place)
def local_Position():
    Place = 'Земля'   # Локальная переменная
    print(Place)
S = input('Введите "система" или что-то другое: ')
if S == 'система':
    global_Position()
else:
    local_Position()

# 9.4 Изменение глобальной переменной с помощью global
Number = 10
def change():
    global Number
    Number = 20
print(Number)
change()
print(Number)

# Листинг 10: Лямбда-функция
g = lambda x: x ** 2
print(g(2))

# Листинг 11: Функция map для преобразования строк в числа
old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(map(int, old_list))
print(new_list)

# Листинг 12: Функция map с пользовательской функцией и с lambda
def miles_to_kilometers(num_miles):
    return num_miles * 1.6
mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(miles_to_kilometers, mile_distances))
print(kilometer_distances)
# То же самое через lambda
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))
print(kilometer_distances)

# Листинг 13: Функция map с несколькими списками
l1 = [1, 2, 3]
l2 = [4, 5, 6]
new_list = list(map(lambda x, y: x + y, l1, l2))
print(new_list)
# Списки разной длины
l1 = [1, 2, 3]
l2 = [4, 5]
new_list = list(map(lambda x, y: x + y, l1, l2))
print(new_list)

# Листинг 14: Функция filter
mixed = ['mak', 'proco', 'mak', 'mak', 'proco', 'mak', 'proco', 'proco', 'proco', 'mak']
zolushka = list(filter(lambda x: x == 'mak', mixed))
print(zolushka)

# Листинг 15: Функция reduce (сумма и максимум)
from functools import reduce
items = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, items)
print(sum_all)
items = [1, 24, 17, 14, 9, 32, 2]
all_max = reduce(lambda a, b: a if (a > b) else b, items)
print(all_max)

# Листинг 16: Функция zip
a = [1, 2, 3]
b = "xyz"
c = (None, True)
res = list(zip(a, b, c))
print(res)