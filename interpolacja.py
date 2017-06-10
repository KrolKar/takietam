# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:22:51 2017

@author: student
"""

import numpy as np
from matplotlib import pyplot as plt

def wsp(x,y):
    deg = len(x) - 1
    for i in range(1, deg + 1, 1):
        print(i, ":")
        for poczatek in range(1, deg + 1, 1):
            koniec = poczatek + i
            if koniec > deg + 1:
                continue
            for j in range(poczatek, koniec, 1):
                print(j, end = ' ')
            print()

def wsp2(x,y):
    deg = len(x) - 1
    n = len(y)
    wspl = np.zeros((deg, deg + 1, 2))
    for i in range(deg ):
        n = n - 1
        for poczatek in range(deg ):
            koniec = poczatek + i
            if koniec > deg :
                continue
            wspl[poczatek, i, 0] = x[poczatek]
            wspl[poczatek, i, 1] = x[koniec]
    return wspl


def wspb(x, y):
    deg = len(x) - 1
    b = []
    fz = y
    fw = []
    b.append(y[1])
    #print(b[0])
    for i in range(1, deg + 1, 1):
        fw = np.zeros(len(fz) - 1)
        for j in range(len(fz) - 1):
            fw[j] = (fz[j + 1] - fz[j])/(x[i] - x[0])
        b.append(fw[0])
        #print(fw[0])
        fz = fw
    return b

def wspb2(x,y):
    deg = len(x) - 1
    n = len(y)
    b = []
    f = np.zeros((n,deg + 1))
    f[:,0] = y
    for i in range(len(y) ):#- 1):
        f[0, i] = y[i]
    b.append(f[0,0])
    X = wsp2(x, y)
    for i in range(deg):
        n = n - 1
        for j in range(n):
            f[j,i] = (f[j , i ] - f[j + 1, i ])/(iksy[j, i, 0] - iksy[j, i, 1])

        b.append(f[0,i])
        print(f)
    return b

def licNew(x, b, t):
    y =[]
    deg = len(x) - 1
    for i in range(len(t)):
        yt = 0
        mnoz = 1
        yt = b[0] + b[1] * (t[i] - x[0]) + b[2] * (t[i] - x[0])  * (t[i] - x[1]) + b[2] * (t[i] - x[0]) * (t[i] - x[1]) * (t[i] - x[2])
        yt = yt + b[3] * (t[i] - x[0]) * (t[i] - x[1]) * (t[i] - x[2]) * (t[i] - x[3]) + b[4] * (t[i] - x[0]) * (t[i] - x[1]) * (t[i] - x[2]) * (t[i] - x[3]) * (t[i] - x[4])
        yt = yt + b[5] * (t[i] - x[0]) * (t[i] - x[1]) * (t[i] - x[2]) * (t[i] - x[3]) * (t[i] - x[4]) * (t[i] - x[5])
        yt = yt + b[6] * (t[i] - x[0]) * (t[i] - x[1]) * (t[i] - x[2]) * (t[i] - x[3]) * (t[i] - x[4]) * (t[i] - x[5]) * (t[i] - x[6])
        yt = yt + b[7] * (t[i] - x[0]) * (t[i] - x[1]) * (t[i] - x[2]) * (t[i] - x[3]) * (t[i] - x[4]) * (t[i] - x[5]) * (t[i] - x[6]) * (t[i] - x[7])
        yt = yt + b[8] * (t[i] - x[0]) * (t[i] - x[1]) * (t[i] - x[2]) * (t[i] - x[3]) * (t[i] - x[4]) * (t[i] - x[5]) * (t[i] - x[6]) * (t[i] - x[7]) * (t[i] - x[8])
        yt = yt + b[9] * (t[i] - x[0]) * (t[i] - x[1]) * (t[i] - x[2]) * (t[i] - x[3]) * (t[i] - x[4]) * (t[i] - x[5]) * (t[i] - x[6]) * (t[i] - x[7]) * (t[i] - x[8]) * (t[i] - x[9])
        #for j in range(deg):
        #   mnoz = mnoz * (t[i] - x[j])
        #   yt = yt + b[j] * mnoz

        y.append(yt)
        #print(y)
    return y

def przedzial(x1, x2, y1, y2, x):
    a = np.array([[1, x1, x1**2, x1**3  ],
                  [1, x2, x2**2, x2**3  ],
                  [0, 1,  2*x2,  3*x2**2],
                  [0, 1,  2*x1,  3*x1**2]])
    b = np.array([y1, y2, 0, 0])
    w = np.linalg.solve(a, b)
    return w[0] + w[1] * x + w[2] * x**2 + w[3] * x**3

def funSklejana(x, y, t):
    Y = []
    for i in range(len(t)):
        for j in range(len(x) - 1):
            if x[j] <=  t[i] and x[j+1] > t[i]:
                Y.append(przedzial(x[j], x[j+1], y[j], y[j+1], t[i]))
    return Y

dataFile = open("data8.txt", 'r')
dataplt = dataFile.read()

dataplt = dataplt.split()
dataplt = np.array(dataplt)
dataplt = dataplt.astype(np.float)

x = dataplt[0::2]
y = dataplt[1::2]

iksy = np.array([[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],
                 [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [0, 0]],
                 [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9], [7, 10], [0, 0], [0, 0]],
                 [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [0, 0], [0, 0], [0, 0]],
                 [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [0, 0], [0, 0], [0, 0], [0, 0]],
                 [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                 [[0, 7], [1, 8], [2, 9], [3, 10], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                 [[0, 8], [1, 9], [2, 10], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                 [[0, 9], [1, 10], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                 [[0, 10], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]])

b = wspb2(x,y)
t = np.linspace(-12, 7.5, num=100)
t2 = np.linspace(-12, 7.5, num=100)
Y = licNew(x, b, t)
Y2 = licNew(x, b, x)
Y3 = funSklejana(x, y, t)

print(b)

plt.plot(x, y, 'rx')
plt.plot(t, Y, 'b')
#plt.plot(x, Y2, 'bx')
plt.plot(t2, Y3, 'y')
plt.show()