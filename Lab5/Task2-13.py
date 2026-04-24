# 9 вариант

# 2 задание
print("\nЗадание 2\n")

def f(x):
    return x**3 - 3*x + 3

x = float(input("Введите значение x: "))
y = f(x)
print(f"f({x}) = {y}")

# 9 вариант
import math

# 3 задание
print("\nЗадание 3\n")

def z1(x, y):
    return math.sin(x + 0.5) - y - 1

def z2(x, y):
    return x + math.cos(y - 2)

x = float(input("Введите x: "))
y = float(input("Введите y: "))

print(f"z1({x}, {y}) = {z1(x, y)}")
print(f"z2({x}, {y}) = {z2(x, y)}")

# 4 задание
print("\nЗадание 4\n")

def sum_three_digits(n):
    return n // 100 + (n // 10) % 10 + n % 10

print("Все шестизначные счастливые номера:")
for num in range(100000, 1000000):
    first = num // 1000
    last = num % 1000
    if sum_three_digits(first) == sum_three_digits(last):
        print(num)

# 5 задание
print("\nЗадание 5\n")

def even_stats_list(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    if not evens:
        return None, 0
    return min(evens), sum(evens)

data = [5, 8, 3, 12, 7, 4, 10]
print("Список:", data)
min_even, sum_even = even_stats_list(data)
print(f"Способ 1 (список): мин. чётное = {min_even}, сумма чётных = {sum_even}")

# 6 задание
print("\nЗадание 6\n")

def to_base(num, N):
    digits = "0123456789ABCDEF"
    if num < N:
        return digits[num]
    return to_base(num // N, N) + digits[num % N]

num = int(input("Введите натуральное число: "))
N = int(input("Введите основание системы счисления (2..16): "))

if 2 <= N <= 16:
    result = to_base(num, N)
    print(f"Число {num} в системе с основанием {N} = {result}")
else:
    print("Ошибка: основание должно быть от 2 до 16.")

# 7 задание
print("\nЗадание 7\n")

def is_prime_recursive(n, divisor=None):
    if divisor is None:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        divisor = 3
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor + 2)

num = int(input("Введите натуральное число: "))

if is_prime_recursive(num):
    print(f"{num} — простое число")
else:
    print(f"{num} — составное или не является натуральным >1")

# 8 задание
print("\nЗадание 8 \n")

# Задание 8: список вещественных чисел, остатки от деления на 7 через map и lambda

numbers = [10.5, 14.3, 7.0, 21.8, 5.2, 49.0, 3.14]
remainders = list(map(lambda x: x % 7, numbers))
print("Исходный список:", numbers)
print("Остатки от деления на 7:", remainders)

# 9 задание
print("\nЗадание 9 \n")

names = ['катя', 'маша', 'таня', 'саша']
print("Первоначальный список", names)
capitalized_names = list(map(lambda name: name.capitalize(), names))
print("Изменённый список", capitalized_names)

# 10 задание
print("\nЗадание 10 \n")

names = ['Маша', 'Петя', 'Вася']
names = list(map(lambda name: hash(name), names))
print(names)

# 11 задание
print("\nЗадание 11 \n")

from functools import reduce

sentences = [
    'научиться плести рыболовные сети',
    'обучать нейронные сети',
    'паук ловит в сети мух'
]

total_count = reduce(lambda acc, s: acc + s.count('сети'), sentences, 0)
print(total_count)  # => 3

# 12 задание
print("\nЗадание 12 \n")

numbers = [14, 23, 49, 56, 78, 70, 93, 105, 8, 21]
multiples_of_7 = list(filter(lambda x: x % 7 == 0, numbers))

print("Исходный список:", numbers)
print("Числа, кратные 7:", multiples_of_7)

# 13 задание
print("\nЗадание 13 \n")

names = [
    'Василий Акимович Кузнецов',
    'Петр Николаевич Чириков',
    'Анна Сергеевна Иванова',
    'Дмитрий Петрович Соколов'
]
math_scores = [85, 79, 92, 68]
russian_scores = [42, 49, 78, 55]
informatics_scores = [65, 78, 88, 47]

# Составление списка кортежей с помощью zip
students = list(zip(names, math_scores, russian_scores, informatics_scores))
print(students)