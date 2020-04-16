import numpy as np
import math
import matplotlib.pyplot as plt

xt = np.linspace(0, 1, 20)
n = [3, 10, 30]


def fourier(values, order):
    i = np.arange(1, order+1)[:, np.newaxis].T
    values = values[:, np.newaxis]
    S = (1 / ((2 * i) - 1)) * np.sin(((2 * i) - 1) * 2 * math.pi * values) * 4 / math.pi
    S_sum = np.sum(S, axis=1)
    return S_sum


for n_val in n:
    plt.plot(xt, fourier(xt, n_val), label=n_val)
plt.legend()
plt.show()
