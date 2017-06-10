# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:25:33 2017

@author: student
"""
import matplotlib.pyplot as plt
import numpy as np
from sympy import diff, symbols


def Y(x):
    y1 = -x ** 2 - 5 * x - 3

    y2 = (-2 * x ** 2) / (3 * x + 2)
    return y1 - y2


def y1(x):
    return (-2 * x ** 2) / (3 * x + 2)

def graf() :
    x = np.arange(-5, 1, 0.01)
    y1 = -x**2 -5*x - 3
    
    y2 = (-2 * x**2)/(3*x +2)
    plt.plot(x,y1, 'b')
    plt.plot(x,y2, 'r')
    plt.grid(True)
    plt.show()
#(-3,2) (-1.3,2) (-0.6,0)

def NR(beg):
    x = symbols('x')
    dY = diff((x**2 + x - 2) - (-(2 * x**2) / (x + 3)), x)

    xx = beg
    for i in range(50):

        if abs(Y(xx)) <= 0.1:
            print(xx, y1(xx))
            return None

        xx = xx - Y(xx)/dY.evalf(subs = {x: xx})
    return None


def iter():
    x = np.arange(-5, 1, 0.01)
    y1 = -x**2 -5*x - 3
    
    y2 = (-2 * x**2)/(3*x +2)
    
    Y = y1-y2
    

    aktualne = Y[1]
    poprzednie = Y[0]
    i=1
    
    for j in Y:
        if (aktualne > 0 and poprzednie < 0) or (aktualne < 0 and poprzednie > 0):
            print(x[i], y1[i])
            return 0
        else:
            i = i + 1
            poprzednie = aktualne
            aktualne = Y[i]

            
            
graf()
print("iteracyjnie")
iter()
print("Newtona-Raphsona")
NR(-3.23)
NR(-0.8)
NR(-0.4806)
           
            
            
            
            