import numpy as np

def gaussian_elimination_32bit(A, b):
    A = A.astype(np.float32)  # Convertir A a float32
    b = b.astype(np.float32)  # Convertir b a float32

    n = len(b)  # Número de ecuaciones

    # Eliminación hacia adelante
    for i in range(n):
        # Pivote para el valor máximo en la columna i para evitar inestabilidad numérica
        max_row = np.argmax(np.abs(A[i:n, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Hacer que la diagonal contenga todos unos
        pivot = A[i, i]
        A[i] = A[i] / pivot
        b[i] = b[i] / pivot

        # Hacer que los elementos debajo del pivote en la columna i sean iguales a cero
        for j in range(i + 1, n):
            factor = A[j, i]
            A[j] -= factor * A[i]
            b[j] -= factor * b[i]

    # Sustitución hacia atrás
    x = np.zeros(n, dtype=np.float32)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] - np.dot(A[i, i + 1:], x[i + 1:])

    return x

# Ejercicio 2
A2 = np.array([
    [3.333, 15920, -10.333],
    [2.222, 16.71, 9.612],
    [1.5611, 5.1791, 1.6852]
], dtype=np.float32)
b2 = np.array([15913, 28.544, 8.4254], dtype=np.float32)

# Resolver el ejercicio 2
sol2 = gaussian_elimination_32bit(A2, b2)

# Resultado
print("Solución del ejercicio 2:", sol2)
