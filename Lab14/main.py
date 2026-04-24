import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Программа для работы с текстовыми файлами: запись текста, чтение, подсчёт слов/строк."
    )

    # Позиционный аргумент: текст для записи (обязательный, но только если не используется --read или --count)
    # Однако argparse не позволяет сделать аргумент условно-обязательным. Поэтому мы сделаем его обязательным,
    # но добавим проверку на конфликт с --read/--count позже. Лучше сделать текст необязательным,
    # а при отсутствии и без флагов чтения/подсчёта выдавать ошибку.
    # Поступим так: сделаем текст позиционным с nargs='?', но проверим в коде.
    parser.add_argument(
        "text", 
        nargs="?", 
        help="Текст для записи в файл (если не указан и нет флагов -r/-c, то ошибка)"
    )

    # Опциональный аргумент для имени файла
    parser.add_argument(
        "-f", "--file", 
        default="Task1_output.txt", 
        help="Имя файла для записи/чтения (по умолчанию: Task1_output.txt)"
    )

    # Флаг чтения файла
    parser.add_argument(
        "-r", "--read", 
        action="store_true", 
        help="Вывести содержимое указанного файла (не изменяя его)"
    )

    # Флаг подсчёта слов и строк
    parser.add_argument(
        "-c", "--count", 
        action="store_true", 
        help="Подсчитать количество строк и слов в указанном файле"
    )

    args = parser.parse_args()

    # Валидация: если не указан текст и не заданы флаги -r/-c, то ошибка
    if args.text is None and not (args.read or args.count):
        parser.error("Необходимо указать текст для записи или использовать флаги -r/--read или -c/--count.")

    # Если указан флаг --read, выводим содержимое файла и завершаем работу
    if args.read:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print(f"Ошибка: файл '{args.file}' не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
        return

    # Если указан флаг --count, выводим статистику и завершаем
    if args.count:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.splitlines()
                num_lines = len(lines)
                words = content.split()
                num_words = len(words)
                print(f"Файл: {args.file}")
                print(f"Количество строк: {num_lines}")
                print(f"Количество слов: {num_words}")
        except FileNotFoundError:
            print(f"Ошибка: файл '{args.file}' не найден.")
        except Exception as e:
            print(f"Ошибка при подсчёте: {e}")
        return

    # Иначе — запись текста в файл
    try:
        with open(args.file, 'w', encoding='utf-8') as f:
            f.write(args.text)
        print(f"Текст успешно записан в файл '{args.file}'.")
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")

if __name__ == "__main__":
    main()