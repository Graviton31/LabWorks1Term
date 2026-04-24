# Задание 1:
# Реализация алгоритма сортировки вставками
print("Задание 1:")

def insertionsort(L):
    # Проходим по всем элементам, начиная со второго
    for i in range(1, len(L)):
        key = L[i]  # текущий элемент для вставки
        j = i - 1  # индекс предыдущего элемента
        # Сдвигаем элементы, которые больше key, вправо
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key  # вставляем key на правильное место
    return L


L = [3, 6, 8, 2, 9, 1, 7, 0, 5, 9, 4]
print(insertionsort(L))

# Задание 2:
# Реализация алгоритма сортировки слиянием
print("Задание 2:")

def merge(left, right):
    """Слияние двух отсортированных списков"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort(L):
    """Рекурсивная сортировка слиянием"""
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = mergesort(L[:mid])
    right = mergesort(L[mid:])
    return merge(left, right)

L = [3, 6, 8, 2, 9, 1, 7, 0, 5, 9, 4]
print(mergesort(L))

# Задание 3:
print("Задание 3:")

import random

def generate_random_array(length, min_val=0, max_val=100):
    # Возвращает список случайных целых чисел указанной длины.
    return [random.randint(min_val, max_val) for _ in range(length)]

def main():
    try:
        n = int(input("Введите размер массива: "))
        if n <= 0:
            print("Размер должен быть положительным.")
            return
    except ValueError:
        print("Некорректный ввод.")
        return

    arr = generate_random_array(n, 0, 100)
    print("\nИсходный массив:", arr)

    arr1 = arr[:]
    arr2 = arr[:]

    sorted_insertion = insertionsort(arr1)
    print("Сортировка вставками:", sorted_insertion)

    sorted_merge = mergesort(arr2)
    print("Сортировка слиянием:   ", sorted_merge)

    assert sorted_insertion == sorted_merge, "Результаты сортировок различаются!"
    print("\nОбе сортировки работают корректно.")

if __name__ == "__main__":
    main()


# Задание 4:
print("Задание 4:")

def test_sorting_algorithms():

    test_sizes = [0, 1, 5, 10, 20, 50, 100, 200, 500]

    for size in test_sizes:
        # Генерируем случайный массив целых чисел от -100 до 100
        arr = [random.randint(-100, 100) for _ in range(size)]
        # Сортируем копии
        arr_insert = arr[:]
        arr_merge = arr[:]

        sorted_insert = insertionsort(arr_insert)
        sorted_merge = mergesort(arr_merge)

        # Проверяем, что результаты сортировки идентичны
        assert sorted_insert == sorted_merge, f"Ошибка при размере {size}: результаты различаются"

        # Дополнительно – стандартная сортировка для сверки
        assert sorted_insert == sorted(arr), f"Ошибка при размере {size}: сортировка выполена неверно"

        print(f"Размер {size}: тест пройден")

    print("Все тесты успешно завершены!")


# Запуск тестирования
if __name__ == "__main__":
    test_sorting_algorithms()

# Задание 5:
print("Задание 5:")

import time

def measure_time(sort_func, arr):
    """Измеряет время выполнения sort_func на копии массива arr (в миллисекундах)"""
    arr_copy = arr[:]                     # создаём копию, чтобы не изменять исходный
    t1 = time.perf_counter()
    sort_func(arr_copy)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0             # возвращаем время в миллисекундах

def print_times(sizes, repeat=1):

    # Шапка таблицы
    print(f"{'Размер':>8}", end="")
    print(f"{'Вставки (мс)':>15}", end="")
    print(f"{'Слияние (мс)':>15}")
    print("-" * 40)

    for size in sizes:
        # Генерируем случайный массив размера size
        arr = list(range(size))
        random.shuffle(arr)

        time_ins = 0.0
        time_mer = 0.0
        for _ in range(repeat):
            time_ins += measure_time(insertionsort, arr)
            time_mer += measure_time(mergesort, arr)
        time_ins /= repeat
        time_mer /= repeat

        print(f"{size:8}", end="")
        print(f"{time_ins:15.3f}", end="")
        print(f"{time_mer:15.3f}")

if __name__ == "__main__":
    sizes = [10, 100, 500, 1000, 2000, 5000, 10000]
    print_times(sizes, repeat=1)