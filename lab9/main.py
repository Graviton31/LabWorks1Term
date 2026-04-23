import numpy as np

# task 1
print("task 1")
vector1 = np.zeros(15)
print(f"Вектор из 15 нулей: {vector1}\n")

# task 2
print("task 2")
vector2 = np.full(8, 3.2)
print(f"Вектор из 8 элементов, заполненный 3.2: {vector2}\n")

# task 3
print("task 3")
vector3 = np.zeros(15)
vector3[4] = 1 
print(f"Вектор из 15 нулей с пятым элементом = 1: {vector3}\n")

# task 4
print("task 4")
vector4 = np.arange(12, 44) 
print(f"Вектор со значениями от 12 до 43: {vector4}\n")

# task 5
print("task 5")
array5 = np.random.rand(3, 3, 2)
print(f"Массив 3x3x2 со случайными значениями:\n{array5}\n")
print(f"Форма массива: {array5.shape}\n")

# task 6
print("task 6")
array6 = np.random.rand(12, 12)
min_value = np.min(array6)
max_value = np.max(array6)
print(f"Массив 12x12 со случайными значениями (первые 5 строк):\n{array6[:5, :5]}")
print(f"Минимум: {min_value}")
print(f"Максимум: {max_value}\n")

# task 7
print("task 7")
matrix7 = np.ones((6, 6))
matrix7[0, :] = 0
matrix7[-1, :] = 0
matrix7[:, 0] = 0
matrix7[:, -1] = 0
print(f"Матрица 6x6 с 1 внутри и 0 на границах:\n{matrix7}\n")

# task 8
print("task 8")
matrix8 = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            matrix8[i, j] = 1
print(f"Матрица 8x8 в шахматном порядке:\n{matrix8}\n")

# task 9
print("task 9")
chess_pattern = np.array([[1, 0], [0, 1]])
matrix9 = np.tile(chess_pattern, (4, 4))
print(f"Матрица 8x8 в шахматном порядке через tile:\n{matrix9}\n")

# task 10
print("task 10")
matrix_a = np.random.randint(1, 10, (4, 2))
matrix_b = np.random.randint(1, 10, (2, 5))
print(f"Матрица A (4x2):\n{matrix_a}")
print(f"Матрица B (2x5):\n{matrix_b}")
result_matrix = np.dot(matrix_a, matrix_b)
print(f"Результат умножения (4x5):\n{result_matrix}\n")

# task 11
print("task 11")
array11 = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
print(f"Исходный массив: {array11}")
mask = (array11 > 4) & (array11 < 7)
array11[mask] = -array11[mask]
print(f"После смены знака у элементов между 4 и 7: {array11}\n")

# task 12
print("task 12")
matrix12 = np.zeros((6, 6))
for i in range(6):
    matrix12[i, :] = i
print(f"Матрица 6x6 со значениями в строках от 0 до 5:\n{matrix12}\n")

# task 13
print("task 13")
vector13 = np.random.randint(1, 100, 15)
print(f"Исходный вектор: {vector13}")
sorted_vector = np.sort(vector13)
print(f"Отсортированный вектор: {sorted_vector}\n")

# task 14
print("task 14")
array14_1 = np.array([1, 2, 3, 4, 5])
array14_2 = np.array([1, 2, 3, 4, 5])
array14_3 = np.array([1, 2, 3, 4, 6])

print(f"Массив 1: {array14_1}")
print(f"Массив 2: {array14_2}")
print(f"Массив 3: {array14_3}")

are_equal_1_2 = np.array_equal(array14_1, array14_2)
are_equal_1_3 = np.array_equal(array14_1, array14_3)

print(f"Массивы 1 и 2 одинаковы: {are_equal_1_2}")
print(f"Массивы 1 и 3 одинаковы: {are_equal_1_3}\n")

# task 15
print("task 15")
array15 = np.random.randint(1, 20, 12)
print(f"Исходный массив: {array15}")
max_index = np.argmax(array15)
max_value = array15[max_index]
array15[max_index] = -1
print(f"Максимальный элемент {max_value} заменен на -1")
print(f"Результат: {array15}\n")

# task 16
print("task 16")
array16 = np.random.randint(1, 100, 20)
target = 42
print(f"Исходный массив: {array16}")
print(f"Целевое значение: {target}")

nearest_index = np.argmin(np.abs(array16 - target))
nearest_value = array16[nearest_index]

print(f"Ближайшее число: {nearest_value}")
print(f"Разница: {abs(nearest_value - target)}\n")
