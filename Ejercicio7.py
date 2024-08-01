import numpy as np

systems = [
    (np.array([[1/4, 1/5, 1/6], [1/3, 1/4, 1/5], [1/2, 1, 2]], dtype=np.float32), np.array([9, 8, 8], dtype=np.float32)),
    (np.array([[3.333, 15920, -10.333], [2.222, 16.71, 9.612], [1.5611, 5.1791, 1.6852]], dtype=np.float32), np.array([15913, 28.544, 8.4254], dtype=np.float32)),
    (np.array([[1, 1/2, 1/3, 1/4], [1/2, 1/3, 1/4, 1/5], [1/3, 1/4, 1/5, 1/6], [1/4, 1/5, 1/6, 1/7]], dtype=np.float32), np.array([1/6, 1/7, 1/8, 1/9], dtype=np.float32)),
    (np.array([[2, 1, -1, 1, -3], [1, 0, 2, -1, 1], [0, -2, -1, 1, -5], [3, 1, -4, 0, 5], [1, -1, -1, -1, 1]], dtype=np.float32), np.array([7, 2, -5, 6, -3], dtype=np.float32))
]

def gauss_jordan(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float).reshape(-1, 1)
    augmented_matrix = np.hstack((A, b))

    for i in range(n):
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
        for j in range(n):
            if i != j:
                augmented_matrix[j] -= augmented_matrix[i] * augmented_matrix[j, i]

    return augmented_matrix[:, -1]

# Resolver cada sistema con Gauss-Jordan
solutions_gj = [gauss_jordan(A, b) for A, b in systems]
for i, sol in enumerate(solutions_gj):
    print(f'Sistema {i+1} (Gauss-Jordan): {sol}')
