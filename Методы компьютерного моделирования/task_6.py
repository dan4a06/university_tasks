import numpy as np

def gaussian_elimination(n, A, B):
    """
    Решает систему линейных уравнений Ax = B методом Гаусса
    
    Параметры:
    n - размерность системы
    A - матрица коэффициентов (n x n)
    B - вектор свободных членов (n x 1)
    
    Возвращает:
    X - вектор решений (n x 1)
    """
    # Создаем расширенную матрицу
    augmented = np.zeros((n, n + 1))
    augmented[:, :n] = A
    augmented[:, n] = B.flatten()
    
    # Прямой ход (приведение к треугольному виду)
    for i in range(n):
        # Поиск максимального элемента в столбце для устойчивости
        max_row = i + np.argmax(np.abs(augmented[i:, i]))
        
        # Перестановка строк
        if max_row != i:
            augmented[[i, max_row]] = augmented[[max_row, i]]
        
        # Проверка на вырожденность
        if abs(augmented[i, i]) < 1e-10:
            raise ValueError("Матрица вырождена или близка к вырожденной")
        
        # Нормализация текущей строки
        augmented[i] = augmented[i] / augmented[i, i]
        
        # Исключение переменной из остальных строк
        for j in range(i + 1, n):
            factor = augmented[j, i]
            augmented[j] = augmented[j] - factor * augmented[i]
    
    # Обратный ход
    X = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):
        X[i, 0] = augmented[i, n] - np.dot(augmented[i, i+1:n], X[i+1:, 0])
    
    return X