import numpy as np
import matplotlib.pyplot as plt

def plot_system():
    x = np.linspace(-10, 10, 400)
    y1 = -2 - 2 * x
    y2 = 2 - x
    y3 = (5 - x) / 3

    plt.figure()
    plt.plot(x, y1, label='')
    plt.plot(x, y2, label='')
    plt.xlabel('')
    plt.ylabel('')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.title('Ejercicio c')
    plt.show()
plot_system()
