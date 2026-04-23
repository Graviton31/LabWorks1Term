import os

# task 1
print("task 1")
with open("input1.txt", "w") as f:
    f.write("2\n2\n")
with open("input1.txt", "r") as f:
    a = int(f.readline().strip())
    b = int(f.readline().strip())
with open("output1.txt", "w") as f:
    f.write(str(a + b))
print("Сумма записана в output1.txt")

# task 2
print("\ntask 2")
with open("input2.txt", "w") as f:
    f.write("Hello world\nPython programming\n")
char = input("Введите символ для поиска: ")
found = False
with open("input2.txt", "r") as f:
    if char in f.read():
        found = True
print("Yes" if found else "No")

# task 3
print("\ntask 3")
with open("input3.txt", "w") as f:
    f.write("1 2 3\n4 5\n6 7 8 9\n")
with open("input3.txt", "r") as f:
    for line_num, line in enumerate(f, 1):
        numbers = list(map(int, line.split()))
        print(f"Сумма в строке {line_num}: {sum(numbers)}")

# task 4
print("\ntask 4")
with open("input4.txt", "w") as f:
    f.write("Hello world\nPython is great\nProgramming\n")
letters = 0
words = 0
lines = 0
with open("input4.txt", "r") as f:
    for line in f:
        lines += 1
        words += len(line.split())
        letters += sum(1 for c in line if c.isalpha())
print(f"Букв: {letters}, Слов: {words}, Строк: {lines}")

# task 5
print("\ntask 5")
with open("file5.txt", "w") as f:
    f.write("Строка 1\nСтрока 2\nСтрока 3\nСтрока 4\nСтрока 5\nСтрока 6\nСтрока 7\n")
lines = []
with open("file5.txt", "r") as f:
    lines = [line.rstrip('\n') for line in f]
print("а) первая строка:", lines[0] if lines else "")
print("б) пятая строка:", lines[4] if len(lines) > 4 else "")
print("в) первые 5 строк:", lines[:5])
s1, s2 = 2, 4
print(f"г) строки с {s1}-й по {s2}-ю:", lines[s1-1:s2] if len(lines) >= s2 else "")
print("д) весь файл:", lines)

# task 6
print("\ntask 6")
with open("file6.txt", "w") as f:
    f.write("Короткая строка\nОчень длинная строка для проверки\nСредняя\n")
lines = []
with open("file6.txt", "r") as f:
    lines = [line.rstrip('\n') for line in f]
if lines:
    lengths = [len(line) for line in lines]
    max_len = max(lengths)
    longest_indices = [i for i, l in enumerate(lengths) if l == max_len]
    print(f"а) Длина самой длинной строки: {max_len}")
    print(f"б) Номер самой длинной строки (первой): {longest_indices[0] + 1}")
    print(f"в) Самая длинная строка: {lines[longest_indices[0]]}")

# task 7
print("\ntask 7")
with open("input7.txt", "w") as f:
    f.write("abcdef\n12345\nhello\n")
with open("input7.txt", "r") as f:
    lines = [line.rstrip('\n') for line in f]
reversed_chars = [line[::-1] for line in lines]
with open("output7a.txt", "w") as f:
    for line in reversed_chars:
        f.write(line + "\n")
with open("output7b.txt", "w") as f:
    for line in reversed(lines):
        f.write(line + "\n")
print("Строки переписаны в output7a.txt - порядок строк сохранен, символы перевернуты")
print("Строки переписаны в output7b.txt - порядок строк обратный, символы в прямом порядке")

# task 8
print("\ntask 8")
with open("file8a.txt", "w") as f:
    f.write("Строка 1\nСтрока 2\nСтрока 3\n")
with open("file8b.txt", "w") as f:
    f.write("Строка 1\nСтрока X\nСтрока 3\n")
with open("file8a.txt", "r") as f1, open("file8b.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
different_line = None
for i, (l1, l2) in enumerate(zip(lines1, lines2), 1):
    if l1 != l2:
        different_line = i
        break
if different_line:
    print(f"Строки отличаются в строке {different_line}")
else:
    print("Строки совпадают")

# task 9
print("\ntask 9")
input_data = """5
Иванов Сергей 1 5
Сергеев Петр 3 5
Петров Кирилл 1 2
"""
with open("train.txt", "w") as f:
    f.write(input_data)
with open("train.txt", "r") as f:
    lines = f.readlines()
N = int(lines[0].strip())
passengers = []
for line in lines[1:]:
    if line.strip():
        parts = line.split()
        get_on = int(parts[-2])
        get_off = int(parts[-1])
        passengers.append((get_on, get_off))
segments = [0] * (N - 1)
for get_on, get_off in passengers:
    for i in range(get_on - 1, get_off - 1):
        segments[i] += 1
max_passengers = max(segments) if segments else 0
print("Перегоны с наибольшим числом пассажиров:")
for i, count in enumerate(segments):
    if count == max_passengers and max_passengers > 0:
        print(f"{i+1}-{i+2}")
