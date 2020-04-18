# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:56:52 2020

@author: james
"""

import numpy as np
import matplotlib.pyplot as plt

data1 = np.random.randint(-4, 4, 100)
data1[50] += -20
data1[51] += -20
data1[52] += -20
print(data1)


def expofilter(datae, alpha):
    f = np.copy(datae)
    for i in range(0, len(f)-1):
        f[i+1] = alpha * f[i] + (1 - alpha) * f[i+1]
    return f


def changeDetect(data, alpha, threshold):
    array = expofilter(data, alpha)
    #print(array)
    xval = range(0, len(data))
    #plt.plot(xval, array)
    #plt.show()
    return xval, array, np.where(np.abs(array) > threshold)[0]


#print(changeDetect(data1, 0.95, 1.5))
#print(data1)
plt.figure(1)
for i in range(6):
    xx, yy, _ = changeDetect(data1, 0.75+(i*0.05), 1.5)
    plt.plot(xx,yy, label=0.75+(i*0.05))
plt.legend()
plt.show()
#print(data1)

xval = range(0, len(data1))
yval = expofilter(data1, 0.85)

print(yval)

plt.plot(xval, yval)
plt.show()