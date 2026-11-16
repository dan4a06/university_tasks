import sympy as sp

def matrix_method(A, b):
    """
    Решение СЛАУ Ax = b матричным методом (через обратную матрицу).
    
    Параметры:
        A : sympy.Matrix или список списков — матрица коэффициентов (n x n)
        b : sympy.Matrix или список — вектор свободных членов (n)
        
    Возвращает:
        sympy.Matrix — вектор решения x
    """
    A = sp.Matrix(A)
    b = sp.Matrix(b)
    
    n, m = A.shape
    if n != m:
        raise ValueError("Матрица A должна быть квадратной")
    if b.shape != (n, 1):
        raise ValueError("Вектор b должен иметь размер n x 1")
    
    det_A = A.det()
    if det_A == 0:
        raise ValueError("Определитель матрицы равен нулю — обратная матрица не существует")
    
    # Находим обратную матрицу и умножаем на вектор b
    A_inv = A.inv()
    x = A_inv * b
    
    return x

A = sp.Matrix([
    [ 2,  1, -1],
    [-3, -1,  2],
    [-2,  1,  2]
])
b = sp.Matrix([8, -11, -3])

print("=== Исходные данные ===")
print("Матрица A:")
print(A)
print("\nВектор b:")
print(b)

x = matrix_method(A, b)
print("\nответ")
print(x)