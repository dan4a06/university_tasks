import sympy as sp


def cramer_method(A, b):
    A = sp.Matrix(A)
    b = sp.Matrix(b)
    
    n, m = A.shape
    if n != m:
        raise ValueError("Матрица A должна быть квадратной")
    if b.shape != (n, 1):
        raise ValueError("Вектор b должен иметь размер n x 1")
    
    det_A = A.det()
    if det_A == 0:
        raise ValueError("Определитель матрицы равен нулю — метод Крамера неприменим")
    
    x = sp.zeros(n, 1)
    for i in range(n):
        # Заменяем i-й столбец на вектор b
        A_i = A.copy()
        A_i[:, i] = b
        x[i] = A_i.det() / det_A
    
    return x


A = sp.Matrix([[2, 3],
               [4, -1]])
b = sp.Matrix([13, 5])

x = cramer_method(A, b)
print("x =", x.T)                 # ожидается [2, 3]
print("Тест 1 пройден")

A = sp.Matrix([[2, 1, -1],
               [-3, -1, 2],
               [-2, 1, 2]])
b = sp.Matrix([8, -11, -3])

x = cramer_method(A, b)
print("x =", x.T)                 # ожидается [2, 3, -1]
print("Тест 2 пройден")