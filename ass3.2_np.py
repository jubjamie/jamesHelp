import numpy as np
import math
import matplotlib.pyplot as plt

xt = np.linspace(0, 1, 20)
n = [3, 10, 30]


def fourier(values, order):
    # Creates array [0,1,2...] of order. If order = 3 then i would = 0,1,2 with .shape() (3,) which is 1D
    # The newaxis bit makes it (1,3). Same thing for values but the axis is in the other position to make (20,1) so it can be combined to a 2D
    i = np.arange(1, order+1)[np.newaxis, :]
    values = values[:, np.newaxis]
    # DOne as a 3, 20 matrix
    S = (1 / ((2 * i) - 1)) * np.sin(((2 * i) - 1) * 2 * math.pi * values) * 4 / math.pi
    # Sum in the correct dimension to get 20 long array out not 3.
    S_sum = np.sum(S, axis=1)
    return S_sum


for n_val in n:
    plt.plot(xt, fourier(xt, n_val), label=n_val)
plt.legend()
plt.show()
