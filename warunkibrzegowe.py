import numpy as np
import matplotlib.pyplot as plt

A = np.zeros((81, 81))
b = np.zeros(81)
x = np.zeros(81)
hp = 0.05
Ta = 100

def wsp(p):
    x = p%9
    y = p//9
    return x, y

def sasiad(x, y):
    result = 0
    if x == 0:
       result += 390 - y*10 
    elif x == 8:
        result += 290 - y*10
    elif y == 0:
        result += 390 - x*10
    elif y == 8:
        result += 290 - x*10
    return result

for (p1, p2), _ in np.ndenumerate(A):
    if p1 == p2:
        A[p1, p2] = -(1 + hp)
    x1, y1 = wsp(p1)
    x2, y2 = wsp(p2)
    if abs(x1 - x2) == 1 and abs(y1 - y2) == 0:
        A[p1, p2] = 1/4
    elif abs(x1 - x2) == 0 and abs(y1 - y2) == 1:
        A[p1, p2] = 1/4
         
for p, _ in enumerate(b):
    x, y = wsp(p)
    b[p] = -hp * Ta - 1/4 * sasiad(x, y)

print(A)
print(b)
x = np.linalg.solve(A, b)
print(x)        

X = []
Y = []
Z = np.zeros((9,9))
C = []
tx = []
ty = []
maxcolor = 400

for p, c in enumerate(x):
    px, py = wsp(p)
    X.append(px)
    Y.append(py)
    c = c/maxcolor
    color = (c, 0, 0)
    C.append(color)
    Z[px, py] = x[p]
    #plt.plot(px, py, 'o', color = color)
X = range(9)
Y = range(9)
Z = x.reshape((9,9))
plt.contour(X,Y,Z)    
plt.show()





