import random

def generate_matrix(rows, cols, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны иметь одинаковые размеры для сложения")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

a = int(input("введите колличество столбцов матроицы: "))
b = int(input("введите колличество строк матроицы: "))

matrix1 = generate_matrix(a, b, -200, 200)
matrix2 = generate_matrix(a, b, -200, 200)

matrix3 = add_matrices(matrix1, matrix2)

print("Матрица 1:")
for row in matrix1:
    print(row)

print("\nМатрица 2:")
for row in matrix2:
    print(row)

print("\nМатрица 3 (Результат):")
for row in matrix3:
    print(row)
