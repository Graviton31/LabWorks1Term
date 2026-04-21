import random

# task 1
print("task 1")
heights = [random.randint(163, 190) for _ in range(12)]
print(f"Список ростов: {heights}")

# task 2
print("\ntask 2")
a = int(input("Введите первый член прогрессии a: "))
p = int(input("Введите разность прогрессии p: "))
progression = [a + i * p for i in range(10)]
print(f"Десять первых членов прогрессии: {progression}")

# task 3
print("\ntask 3")
t3list = [1, 2, 3, 4, 5]
print(f"Исходный список: {t3list}")
print(f"Список в обратном порядке: {t3list[::-1]}")

# task 4
print("\ntask 4")
a = [5, 3, 8, 1, 9, 2]
print(f"Исходный список: {a}")
result = 0
sign = 1
for elem in a:
    result += sign * elem
    sign = -sign
print(f"Знакопеременная сумма = {result}")

# task 5
print("\ntask 5")
class_sizes = [random.randint(15, 35) for _ in range(42)]
total_students = sum(class_sizes)
print(f"Общее число учеников: {total_students}")
if 1000 <= total_students <= 9999:
    print("Верно, общее число учеников является четырехзначным")
else:
    print("Неверно, общее число учеников не является четырехзначным")

# task 6
print("\ntask 6")
numbers = [12, 25, 30, 47, 50, 63, 70, 81, 90, 100]
print(f"Исходный список: {numbers}")
print("а) Все четные элементы:", [x for x in numbers if x % 2 == 0])
print("б) Все элементы, оканчивающиеся нулем:", [x for x in numbers if x % 10 == 0])

# task 8
print("\ntask 8")
sorted_list = [10, 10, 9, 8, 8, 7, 7, 7, 6, 5, 5, 4, 3, 2, 2, 1]
print(f"Список (по не возрастанию): {sorted_list}")
unique_count = len(set(sorted_list))
print(f"Число различных элементов: {unique_count}")

# task 9
print("\ntask 9")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Исходный список: {arr}")
p1 = 0, p2 = 1
for i in range (len(arr)):
    arr[p1], arr[p2] = arr[p2], arr[p1]
    p1 = p1 + 1
    p2 = p2 + 1
print(f"После перестановки соседних элементов: {arr}")

# task 12
print("\ntask 12")
shoe_sizes = [38, 40, 42, 40, 39, 41, 38, 42, 43, 40, 39, 41, 42, 38, 40]
print(f"Размеры обуви спортсменов: {shoe_sizes}")
unique_sizes = sorted(set(shoe_sizes))
print(f"Различные размеры для заказа: {unique_sizes}")

# task 14
print("\ntask 14")
grades = [5, 4, 5, 3, 2, 5, 4, 3, 5, 5, 4, 2, 2, 3]
print(f"Оценки Васи: {grades}")
average_grade = sum(grades) / len(grades)
print(f"Средний балл: {average_grade:.2f}")
formatted_grades = "; ".join(str(g) for g in grades)
print(f"Оценки в формате: {formatted_grades}")

# task 15
print("\ntask 15")
numbers_divisible = [x for x in range(1, 10001) if (x % 7 == 0 and x % 3 == 0) or x % 9 == 0]
print(f"Числа, делящиеся на 7 и 3 или на 9 (первые 20): {numbers_divisible[:20]}")
print(f"Всего таких чисел: {len(numbers_divisible)}")

# task 16
print("\ntask 16")
n = 10
power_list = [int(str(i)*2) for i in range(1, n+1)]
print(f"Список: {power_list}")

# task 17
print("\ntask 17")
nested_list = [[1, 10], [2, 20], [3, 30], [4, 40]]
print(f"Исходный список: {nested_list}")
flattened = [item for sublist in nested_list for item in sublist]
print(f"После преобразования: {flattened}")