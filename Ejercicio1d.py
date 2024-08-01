import numpy as np
import matplotlib.pyplot as plt

def plot_system():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define planos
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)

    Z1 = 1 - 2*X - Y
    Z2 = -1 - 2*X - 4*Y

    ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100)
    ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100)

    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_zlabel('')

    plt.title('Ejercicio d')
    plt.show()
plot_system()
