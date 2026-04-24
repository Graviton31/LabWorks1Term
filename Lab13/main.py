import re

# task 2
def replace_dots_with_page(text):
    pattern = r'\.{2,}'
    replacement = ' - стр. '
    
    edited_text = re.sub(pattern, replacement, text)
    return edited_text


# task 3
def remove_last_dot_in_numbering(text):
    pattern = r'^(\s*\d+(?:\.\d+)*)\.(?=\s+[А-Яа-я])'
    
    replacement = r'\1'
    
    lines = text.split('\n')
    edited_lines = []
    
    for line in lines:
        edited_line = re.sub(pattern, replacement, line)
        edited_lines.append(edited_line)
    
    return '\n'.join(edited_lines)


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"✓ Файл '{filename}' успешно прочитан")
        return content
    except FileNotFoundError:
        print(f"✗ Ошибка: Файл '{filename}' не найден")
        return None
    except Exception as e:
        print(f"✗ Ошибка при чтении файла '{filename}': {e}")
        return None


def write_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✓ Файл '{filename}' успешно записан")
        return True
    except Exception as e:
        print(f"✗ Ошибка при записи файла '{filename}': {e}")
        return False


def create_original_file():

    original_content = """Введение................................................................6
        1. Анализ предметной области..................8
        2. Подготовка набора данных ................................................12
        2.1. Сбор данных..............................................12
        2.2. Очистка данных....................................................14
        2.3. Аугментация данных..........................................17
        2.4. Формирование датасета................................................19
        3. Проектирование нейронной сети..............21
        4. Реализация нейронной сети. Обучение нейронной сети.................................................26
        5. Тестирование приложения..30
        Заключение........35"""
    write_file("Оглавление.txt", original_content)


def main():
    print("=" * 60)
    print("НАЧАЛО ОБРАБОТКИ ТЕКСТА")
    print("=" * 60)
    
    print("\n1. Проверка наличия исходного файла...")
    import os
    if not os.path.exists("Оглавление.txt"):
        print("   Файл 'Оглавление.txt' не найден. Создаем...")
        create_original_file()
    else:
        print("   Файл 'Оглавление.txt' уже существует")
    
    print("\n2. Чтение исходного файла...")
    text = read_file("Оглавление.txt")
    if text is None:
        return
    
    print("\nИсходный текст:")
    print("-" * 60)
    print(text)
    print("-" * 60)
    
    # task 2
    print("\n3. Задание 2: Замена точек на ' - стр. '...")
    edited_text = replace_dots_with_page(text)
    
    # task 2
    print("\n4. Сохранение результата задания 2...")
    write_file("Оглавление_ред.txt", edited_text)
    
    print("\nТекст после задания 2 (замена точек):")
    print("-" * 60)
    print(edited_text)
    print("-" * 60)
    
    # task 3
    print("\n5. Задание 3: Удаление последней точки в нумерации глав...")
    final_text = remove_last_dot_in_numbering(edited_text)
    
    # Сtask 3
    print("\n6. Сохранение результата задания 3...")
    write_file("Оглавление_ред_ред.txt", final_text)
    
    print("\nТекст после задания 3 (удалены точки в номерах глав):")
    print("-" * 60)
    print(final_text)
    print("-" * 60)
    
    print("\n" + "=" * 60)
    print("ОБРАБОТКА ЗАВЕРШЕНА УСПЕШНО!")
    print("=" * 60)
    print("\nСозданные файлы:")
    print("  - Оглавление.txt (исходный)")
    print("  - Оглавление_ред.txt (замена точек на ' - стр. ')")
    print("  - Оглавление_ред_ред.txt (дополнительно удалены точки в номерах)")
    print("=" * 60)


if __name__ == "__main__":
    main()