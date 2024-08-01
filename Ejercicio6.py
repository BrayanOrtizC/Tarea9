import numpy as np
def system_of_species():
    A = np.array([
        [1, 2, 0, 3],
        [1, 0, 2, 2],
        [0, 0, 1, 1]
    ])
    x = np.array([1000, 500, 350, 400])
    b = np.array([3500, 2700, 900])

    # Verificar si hay suficiente alimento
    suficiente_alimento = np.all(np.dot(A, x) <= b)
    print(f"¿Hay suficiente alimento? {'Sí' if suficiente_alimento else 'No'}")

    # Número máximo de animales que se podría agregar
    incrementos_maximos = b - np.dot(A, x)
    print(f"Incrementos máximos posibles: {incrementos_maximos}")

    # Incrementos si la especie 1 se extingue
    A_ext1 = A[:, 1:]
    incrementos_ext1 = b - np.dot(A_ext1, x[1:])
    print(f"Incrementos posibles si la especie 1 se extingue: {incrementos_ext1}")

    # Incrementos si la especie 2 se extingue
    A_ext2 = np.delete(A, 1, axis=1)
    incrementos_ext2 = b - np.dot(A_ext2, np.delete(x, 1))
    print(f"Incrementos posibles si la especie 2 se extingue: {incrementos_ext2}")

system_of_species()
