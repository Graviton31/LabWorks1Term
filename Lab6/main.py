# Задание 1: Дан список чисел, введенных с клавиатуры.
# Определить, сколько раз встречаются различные цифры.

print("\nЗадание 1 \n")

# Ввод списка чисел через пробел
input_str = input("Введите список чисел через пробел: ")
# Разбиваем строку на отдельные элементы (числа могут быть целыми)
numbers = input_str.split()

# Словарь для подсчета вхождений каждой цифры
digit_count = {}

# Перебираем все числа
for num in numbers:
    # Для каждого числа проходим по всем символам (цифрам)
    for digit in num:
        # Игнорируем знак минус, если число отрицательное
        if digit.isdigit():
            digit_count[digit] = digit_count.get(digit, 0) + 1

# Вывод результатов
print("Вхождения цифр:")
for digit in sorted(digit_count.keys()):
    print(f"Цифра '{digit}' встречается {digit_count[digit]} раз(а)")


# Задание 2: Даны два списка чисел, введенных с клавиатуры.
# Определить, сколько и каких чисел одновременно встречается в двух списках.

print("\nЗадание 2 \n")

# Ввод первого списка
input1 = input("Введите числа первого списка через пробел: ")
list1 = list(map(int, input1.split()))

# Ввод второго списка
input2 = input("Введите числа второго списка через пробел: ")
list2 = list(map(int, input2.split()))

# Преобразуем списки в множества
set1 = set(list1)
set2 = set(list2)

# Находим пересечение (числа, присутствующие в обоих множествах)
common = set1 & set2

# Вывод результатов
print(f"Количество чисел, встречающихся в обоих списках: {len(common)}")
if common:
    print("Эти числа:", sorted(common))


# Задание 3: Дан текст, состоящий из строк. Определить количество слов в тексте.
# Словом считается последовательность символов, слова разделены пробелом или символом конца строки.
# Используйте множества (для демонстрации – подсчёт уникальных слов).

print("\nЗадание 3 \n")

print("Введите текст (пустая строка для завершения):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = ' '.join(lines)
words = text.split()
print(f"Общее количество слов: {len(words)}")
print(f"Уникальных слов: {len(set(words))}")


# Задание 4: определить языки, которые знают все школьники, и языки,
# которые знает хотя бы один школьник. Использовать множества.

print("\nЗадание 4 \n")

n = int(input("Введите количество школьников: "))

# Инициализация: множество языков, которые знают все (изначально берём первое)
common_languages = None
# Множество языков, которые знает хотя бы один
any_languages = set()

for i in range(n):
    lang_count = int(input(f"Сколько языков знает {i + 1}-й школьник? "))
    student_langs = set()
    for j in range(lang_count):
        lang = input(f"Язык {j + 1}: ")
        student_langs.add(lang)

    # Обновляем множество "хотя бы один"
    any_languages.update(student_langs)

    # Обновляем множество "все"
    if common_languages is None:
        common_languages = student_langs.copy()
    else:
        common_languages.intersection_update(student_langs)

# Вывод
print("\nРезультат:")
if common_languages:
    print(len(common_languages))
    for lang in sorted(common_languages):
        print(lang)
else:
    print(0)

print(len(any_languages))
for lang in sorted(any_languages):
    print(lang)


# Задание 5: Даны два множества чисел.
# Выведите третье, состоящее из элементов первого и элементов второго множества, которых нет в первом.
# Это объединение множеств.

print("\nЗадание 5 \n")

# Ввод первого множества
input1 = input("Введите числа первого множества через пробел: ")
set1 = set(map(int, input1.split()))

# Ввод второго множества
input2 = input("Введите числа второго множества через пробел: ")
set2 = set(map(int, input2.split()))

# Вычисляем третье множество (объединение)
set3 = set1 | set2

print("Третье множество:", set3)


# Задание 6: подсчёт количества каждого слова в тексте с использованием словаря

print("\nЗадание 6 \n")

n = int(input("Введите количество строк: "))
word_count = {}

for i in range(n):
    line = input()
    words = line.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

print("\nРезультат (слово -> количество):")
for word in sorted(word_count.keys()):
    print(f"{word}: {word_count[word]}")


# Задание 7: найти самое длинное слово в тексте с использованием словаря

print("\nЗадание 7 \n")

n = int(input("Введите количество строк: "))
words_dict = {}  # слово -> его длина

for i in range(n):
    line = input()
    words = line.split()
    for word in words:
        words_dict[word] = len(word)

# Находим самое длинное слово (если несколько, берём первое)
max_word = max(words_dict, key=words_dict.get)  # по значению длины
print(f"Самое длинное слово: {max_word} (длина {words_dict[max_word]})")


# Задание 8: найти слово, которое встречается в тексте чаще всего, используя словарь

print("\nЗадание 8 \n")

n = int(input("Введите количество строк: "))
word_count = {}

for i in range(n):
    line = input()
    words = line.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

# Находим слово с максимальной частотой
max_word = max(word_count, key=word_count.get)  # слово с наибольшим значением
max_freq = word_count[max_word]

print(f"Слово '{max_word}' встречается {max_freq} раз(а)")


# Задание 9: учёт продаж спортивного интернет-магазина.
# Каждая строка: ФИО товар количество
# Ввод завершается пустой строкой.

print("\nЗадание 9 \n")

print("Введите данные о продажах (Фамилия, товар, количество), пустая строка для завершения:")
sales = {}

while True:
    line = input()
    if line == "":
        break
    parts = line.split()
    if len(parts) != 3:
        print("Пропущена некорректная строка (должно быть 3 элемента)")
        continue
    name, product, quantity_str = parts
    quantity = int(quantity_str)

    if name not in sales:
        sales[name] = {}
    inner = sales[name]
    inner[product] = inner.get(product, 0) + quantity

print("\nРезультат:")
for name in sorted(sales.keys()):
    print(name)
    for product, qty in sorted(sales[name].items()):
        print(f"  {product}: {qty}")


# Задание 10: по городу определить область

print("\nЗадание 10 \n")

print("Введите области в формате: Область: город, город, ...")
print("(пустая строка для завершения ввода областей)")
region_map = {}

while True:
    line = input()
    if line == "":
        break
    if ":" not in line:
        continue
    region, cities_str = line.split(":", 1)
    region = region.strip()
    cities = [c.strip() for c in cities_str.split(",")]
    for city in cities:
        region_map[city] = region

print("\nВведите города (по одному на строке, пустая строка для завершения):")
cities = []
while True:
    city = input()
    if city == "":
        break
    cities.append(city.strip())

print("\nРезультат:")
for city in cities:
    print(region_map.get(city, "Город не найден"))