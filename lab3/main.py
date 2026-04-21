# task 1
print("task 1")
kurs = float(input("Введите текущий курс доллара к рублю: "))
for dollar in range(1, 21):
    rub = dollar * kurs
    print(f"{dollar} USD = {rub:.2f} RUB")

# task 2
print("\ntask 2")
n = int(input("Введите число n (от 1 до 9): "))
if 1 <= n <= 9:
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# task 3
print("\ntask 3")
a = int(input("Введите a: "))
b = int(input("Введите b (b >= a): "))
sum_squares = 0
for i in range(a, b + 1):
    sum_squares += i * i
print(f"Сумма квадратов целых чисел от {a} до {b} = {sum_squares}")

# task 4
print("\ntask 4")
num = input("Введите пятизначное число: ")
if len(num) == 5 and num.isdigit():
    reversed_num = num[::-1]
    print(f"Число справа налево: {reversed_num}")
else:
    print("Ошибка: нужно ввести пятизначное число")

# task 5
print("\ntask 5")
n = int(input("Введите n (1 < n <= 10): "))
total_sum = 0
factorial = 1
for k in range(1, n + 1):
    factorial *= k
    total_sum += factorial
print(f"Сумма = {total_sum}")

# task 7
print("\ntask 7")
n = int(input("Введите n (> 1): "))
a, b = 1, 1
while b <= n:
    a, b = b, a + b
print(f"Первое число Фибоначчи, большее {n}: {b}")

# task 8
print("\ntask 8")
num_str = input("Введите натуральное число: ")
min_digit = min(num_str)
count_min = num_str.count(min_digit)
print(f"Минимальная цифра: {min_digit}, встречается {count_min} раз(а)")

# task 9
print("\ntask 9")
n = float(input("Введите n: "))
f = float(input("Введите первый член прогрессии f: "))
s = float(input("Введите шаг прогрессии s: "))
if s == 0:
    if n == f:
        print(f"{n} является членом прогрессии (первый член)")
    else:
        print(f"{n} не является членом прогрессии")
else:
    if (n - f) / s >= 0 and (n - f) % s == 0:
        print(f"{n} является членом арифметической прогрессии")
    else:
        print(f"{n} не является членом арифметической прогрессии")

# task 10 - 11
print("task 10 - 11")
num_str = input("Введите натуральное число с различными цифрами: ")
if len(set(num_str)) == len(num_str):
    max_digit = max(num_str)
    min_digit = min(num_str)
    pos_max = num_str.find(max_digit)
    pos_min = num_str.find(min_digit)
    if pos_max < pos_min:
        print(f"Левее расположена максимальная цифра {max_digit}")
    elif pos_min < pos_max:
        print(f"Левее расположена минимальная цифра {min_digit}")
    else:
        print("Максимальная и минимальная цифра совпадают")

# task 12
print("\ntask 12")
factorial = int(input("Введите факториал числа: "))
n = 1
product = 1
while product < factorial:
    n += 1
    product *= n
if product == factorial:
    print(f"Исходное число: {n}")
else:
    print("Введенное значение не является факториалом целого числа")

# task 15
print("task 15")
n = int(input("Введите натуральное число n: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i ** i
print(f"Сумма = {total_sum}")