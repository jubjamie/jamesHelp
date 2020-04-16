import numpy as np
import math
import matplotlib.pyplot as plt

xt = np.linspace(0, 1, 20)
n = [1, 2, 3, 5, 10, 30]


def fourier(values, order):
    Sarray = []
    print(type(order))
    for j in range(order):
        i = j + 1
        S = (1 / ((2 * i)-1)) * np.sin(((2*i)-1)*2*math.pi*values) * 4 /math.pi
        print(S)
        Sarray.append(S)
        print(Sarray)
    tot = np.sum(Sarray, axis=0)
    print(tot)
    return tot


for n_val in n:
    plt.plot(xt, fourier(xt, n_val), label=n_val)
plt.legend()
plt.show()
