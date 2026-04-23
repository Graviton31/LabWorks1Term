import os
from collections import Counter

# task 1
def find_substr(subst, st):
    return str(subst.lower() in st.lower())

print("task 1")
print(find_substr('Пит', 'пИтон')) 
print(find_substr('программирование', 'ПрограммироВаНИЕ')) 
print(find_substr('Довод', 'Повод')) 

# task 2
def first_last(let, st):
    first = st.find(let)
    last = st.rfind(let)
    return (first, last)

print("\ntask 2")
print(first_last('a', 'abba')) 
print(first_last('a', 'abbaaaab')) 
print(first_last('a', 'a')) 
print(first_last('a', 'spring')) 

# task 3
def most_common_top3(st):
    st_no_spaces = st.replace(' ', '')
    counter = Counter(st_no_spaces)
    most_common = counter.most_common(3)
    result = ', '.join([f"{char} - {count}" for char, count in most_common])
    return result

print("\ntask 3")
print(most_common_top3('Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью'))
print(most_common_top3('АаА'))
print(most_common_top3('Тише едешь — дальше будешь'))

# task 4
def add_text_to_file(st):
    filename = "file.txt"
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(st + '\n')
        return "Файл был создан"
    else:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(st + '\n')
        return "Строка добавлена к существующим"

print("\ntask 4")
if os.path.exists("file.txt"):
    os.remove("file.txt")
print(add_text_to_file("Первая строка"))
print(add_text_to_file("Вторая строка"))
print(add_text_to_file("Третья строка"))

# task 5
def read_from_last(lines, file):
    lines = abs(lines)
    try:
        with open(file, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()

        last_lines = all_lines[-lines:] if lines <= len(all_lines) else all_lines
        for line in last_lines:
            print(line.strip())
    except FileNotFoundError:
        print("Файл не найден")

print("\ntask 5")
read_from_last(2, "file.txt")
print()
read_from_last(-2, "file.txt")

# task 6
def camel(st):
    result = []
    for i, char in enumerate(st):
        if char.isalpha():
            if i % 2 == 0:
                result.append(char.upper())
            else:
                result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)

print("\ntask 6")
print(camel('Копейка рубль бережет'))
print(camel('Из огня да в полымя'))
print(camel('КРАСОТА)))'))

# task 7
def remove_braces(st):
    result = []
    stack = []
    for char in st:
        if char == '(':
            stack.append(len(result))
        elif char == ')' and stack:
            start = stack.pop()
            result = result[:start]
        else:
            if not stack:
                result.append(char)
    return ''.join(result).strip()

print("\ntask 7")
print(remove_braces('Шила(лишнее (лишнее) лишнее) в мешке не утаишь (лишнее)'))
print(remove_braces('(лишнее(лишнее))Шила в мешке не (лишнее(лишнее(лишнее)))утаишь'))

# task 8
def delete_backspace(st):
    result = []
    for char in st:
        if char == '@':
            if result:
                result.pop()
        else:
            result.append(char)
    return ''.join(result)

print("\ntask 8")
print(delete_backspace('пп@олс@кр@овт@оде@ец'))
print(delete_backspace('сварка@@@@@лоб@ну@'))