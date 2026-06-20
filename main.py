import numpy as np
def get_matrix_from_input():
    try:
        rows = int(input("Введите количество строк: "))
        if rows <= 0: raise ValueError("Количество строк должно быть > 0")
        matrix = []
        for i in range(rows):
            row = list(map(float, input(f"Введите элементы {i+1}-й строки через пробел: ").split()))
            matrix.append(row)
            
        if len(set(len(r) for r in matrix)) > 1:
            raise ValueError("Все строки должны иметь одинаковую длину!")
        return matrix
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return None
def calculate_rank(matrix):
    A = np.array(matrix, dtype=float)
    rows, cols = A.shape
    rank = 0
    pivot_row = 0
    for j in range(cols):
        if pivot_row >= rows:
            break
            
        max_idx = np.argmax(np.abs(A[pivot_row:, j])) + pivot_row
        if np.isclose(A[max_idx, j], 0):
            continue
        A[[pivot_row, max_idx]] = A[[max_idx, pivot_row]]
        
        for i in range(pivot_row + 1, rows):
            factor = A[i, j] / A[pivot_row, j]
            A[i, j:] -= factor * A[pivot_row, j:]
            
        pivot_row += 1
        rank += 1
    return rank
matrix_data = get_matrix_from_input()
if matrix_data is not None:
    rank = calculate_rank(matrix_data)
    print(f"Ранг матрицы равен: {rank}")