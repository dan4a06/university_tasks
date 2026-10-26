from sympy import Matrix, symbols, simplify

def gauss(A, B):
    A = Matrix(A)
    B = Matrix(B)
    n = A.rows
    # Расширенная матрица
    M = A.row_join(B)

    # Прямой ход с выбором главного элемента (обход по столбцу)
    for i in range(n):
        # Ищем максимальный по модулю элемент в столбце i начиная со строки i
        pivot_row = max(range(i, n), key=lambda r: abs(M[r, i]))
        if pivot_row != i:
            M.row_swap(i, pivot_row)

        # Обнуляем элементы ниже ведущего
        for j in range(i + 1, n):
            factor = M[j, i] / M[i, i]
            M[j, :] = M[j, :] - factor * M[i, :]

    # Обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = M[i, n]
        for k in range(i + 1, n):
            s -= M[i, k] * x[k]
        x[i] = simplify(s / M[i, i])

    return x


A1 = [[2, 1, -1],
      [-3, -1, 2],
      [-2, 1, 2]]
B1 = [8, -11, -3]
print("Пример 1:", gauss(A1, B1))  # [2, 3, -1]


A2 = [[1, 2, 3],
      [2, 1, 1],
      [3, 2, 1]]
B2 = [14, 7, 11]
print("Пример 2:", gauss(A2, B2))  # [1, 2, 3]



A3 = [[0, 2, 1],
      [1, 1, 1],
      [2, 1, 3]]
B3 = [5, 6, 13]
print("Пример 3:", gauss(A3, B3))  # [2, 1, 3]


a, b = symbols('a b')
A4 = [[1, 1],
      [1, -1]]
B4 = [a + b, a - b]
print("Пример 4:", gauss(A4, B4))  # [a, b]