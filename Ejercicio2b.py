import numpy as np

def gauss_elimination_with_rounding(A, b):
    n = len(A)  # Número de ecuaciones
    M = A.copy()  # Copia de la matriz A

    # Redondeo de los elementos de la matriz y el vector b
    for i in range(n):
        M[i] = [round(elem, 2) for elem in M[i]]
        b[i] = round(b[i], 2)

    # Eliminación Gaussiana
    for k in range(n):
        for i in range(k + 1, n):
            if M[i][k] != 0.0:
                lam = round(M[i][k] / M[k][k], 2)
                M[i] = [round(M[i][j] - lam * M[k][j], 2) for j in range(n)]
                b[i] = round(b[i] - lam * b[k], 2)

    # Sustitución regresiva
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        s = sum(M[i][j] * x[j] for j in range(i, n))
        x[i] = round((b[i] - s) / M[i][i], 2)
    return x

# Sistema
A2 = np.array([
    [4, 2, -1],
    [1/9, 1/2, -1/3],
    [1, 4, 2]
])
b2 = np.array([-5, -1, 9])

# Resolución del sistema
x2 = gauss_elimination_with_rounding(A2, b2)

# Resultado
print("Solución del sistema:", x2)
