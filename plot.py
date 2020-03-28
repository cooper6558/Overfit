from matplotlib import pyplot as plt
import numpy as np


def plot(function, window):
    x = np.linspace(window[0][0], window[0][1], 100)
    y = np.zeros(100)
    for index, value in enumerate(x):
        y[index] = function([value])
    plt.plot(x, y)
    plt.show()
