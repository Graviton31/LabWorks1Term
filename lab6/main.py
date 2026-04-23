import sys
from collections import Counter, defaultdict

# task 1
print("task 1")
numbers = input("Введите список чисел через пробел: ").split()
digit_count = {}
for num in numbers:
    for digit in num:
        if digit.isdigit():
            digit_count[digit] = digit_count.get(digit, 0) + 1
print("Частота встречаемости цифр:")
for digit, count in sorted(digit_count.items()):
    print(f"  Цифра '{digit}': {count} раз(а)")

# task 2
print("\ntask 2")
list1 = input("Введите первый список чисел через пробел: ").split()
list2 = input("Введите второй список чисел через пробел: ").split()
set1 = set(list1)
set2 = set(list2)
common = set1 & set2
common_numbers = [int(x) for x in common if x.lstrip('-').isdigit()]
common_numbers.sort()
print(f"Одновременно встречаются: {len(common_numbers)} чисел")
print(f"Список общих чисел: {common_numbers}")

# task 3
print("\ntask 3")
print("Введите текст (для завершения введите пустую строку):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
text = ' '.join(lines)
words = set(text.split())
print(f"Количество уникальных слов в тексте: {len(words)}")
print(f"Уникальные слова: {sorted(words)[:10]}...")  # показываем первые 10

# task 4
print("\ntask 4")
n = int(input("Введите количество школьников: "))
all_languages = None
at_least_one = set()
for i in range(n):
    k = int(input(f"Введите количество языков для школьника {i+1}: "))
    student_languages = set()
    for j in range(k):
        lang = input(f"  Язык {j+1}: ")
        student_languages.add(lang.lower())
    if all_languages is None:
        all_languages = student_languages.copy()
    else:
        all_languages &= student_languages
    at_least_one |= student_languages
print(f"\nЯзыки, которые знают все школьники ({len(all_languages)}):")
for lang in sorted(all_languages):
    print(f"  {lang}")
print(f"\nЯзыки, которые знает хотя бы один школьник ({len(at_least_one)}):")
for lang in sorted(at_least_one):
    print(f"  {lang}")

# task 5
print("\ntask 5")
set1_input = input("Введите первое множество чисел через пробел: ").split()
set2_input = input("Введите второе множество чисел через пробел: ").split()
set1 = {int(x) for x in set1_input if x.lstrip('-').isdigit()}
set2 = {int(x) for x in set2_input if x.lstrip('-').isdigit()}
result_set = set1 | (set2 - set1)
print(f"Первое множество: {set1}")
print(f"Второе множество: {set2}")
print(f"Результат (элементы первого + элементы второго, которых нет в первом): {result_set}")

# task 6
print("\ntask 6")
n = int(input("Введите количество строк текста: "))
print("Введите текст:")
text_lines = []
for i in range(n):
    line = input()
    text_lines.append(line)
full_text = ' '.join(text_lines)
words = full_text.split()
word_count = Counter(words)
print("\nСтатистика слов:")
for word, count in sorted(word_count.items()):
    print(f"  {word}: {count} раз(а)")

# task 7
print("\ntask 7")
n = int(input("Введите количество строк текста: "))
print("Введите текст:")
text_lines = []
for i in range(n):
    line = input()
    text_lines.append(line)
full_text = ' '.join(text_lines)
words = full_text.split()
if words:
    longest_word = max(words, key=len)
    longest_words = [w for w in words if len(w) == len(longest_word)]
    print(f"Самое длинное слово: {longest_word}")
    print(f"Длина: {len(longest_word)} символов")
    if len(longest_words) > 1:
        print(f"Другие слова такой же длины: {', '.join(set(longest_words))}")
else:
    print("Текст пуст")

# task 8
print("\ntask 8")
n = int(input("Введите количество строк текста: "))
print("Введите текст:")
text_lines = []
for i in range(n):
    line = input()
    text_lines.append(line)
full_text = ' '.join(text_lines)
words = full_text.split()
if words:
    word_count = Counter(words)
    most_common_word, max_count = word_count.most_common(1)[0]
    print(f"Слово, встречающееся чаще всего: '{most_common_word}'")
    print(f"Количество вхождений: {max_count}")
    print(f"Другие частые слова:")
    for word, count in word_count.most_common(5)[1:]:
        print(f"  {word}: {count} раз(а)")
else:
    print("Текст пуст")