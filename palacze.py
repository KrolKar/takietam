# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:21:45 2017

@author: student
"""
import numpy as np
from scipy.linalg import lu
import scipy as sp


E12 = 25
E23 = 50
E35 = 25
E34 = 50

Qa = 200
Qb = 300
Qd =350
Qc = 150

ca = 2
cb = 2

Ws = 1500
Wg = 2500

A = np.array([[-E12-Qa, E12, 0, 0, 0],
                [Qa+E12, -Qa-Qb-E23-E12, E23, 0, 0],
                [0, E23 + Qa + Qb,-E23-E34-Qa-Qb-E35, E34, E35,],
                [0,0,E34+Qc,-E34-Qc,0],
                [0,0,E35+Qd,0,-E35-Qd]])


C = np.array( [[-Ws-Qa*ca],
     [-Qb*cb],
     [0],
     [0],
     [-Wg]])

P, L, U = lu(A)

B = np.linalg.solve(A,C)

print(B)

y = np.linalg.solve(L,C)
b = np.linalg.solve(U,y)

print(b)

Ws = 800
Wg = 1200

Ap = np.array([[-E12-Qa, E12, 0, 0, 0],
                [Qa+E12, -Qa-Qb-E23-E12, E23, 0, 0],
                [0, E23 + Qa + Qb,-E23-E34-Qa-Qb-E35, E34, E35,],
                [0,0,E34+Qc,-E34-Qc,0],
                [0,0,E35+Qd,0,-E35-Qd]])
C = np.array( [[-Ws-Qa*ca],
     [-Qb*cb],
     [0],
     [0],
     [-Wg]])
B = np.linalg.solve(Ap,C)
print("po zmianie")
print(B)
A1=np.linalg.inv(A)
print(A1)

odwr = sp.linalg.inv(A)

print("odwrócona")
print(odwr)

palacze = 100*odwr[3, 0]*Ws/B[3]
grill = 100*odwr[3, 4]*Wg/B[3]
ulica = 100*(Qa*ca*odwr[3,0] + Qb*cb*odwr[3,1])/B[3]

print(odwr [3,0])
print(odwr [3,4])
print(odwr [3,1])
print (Ws, b [3])
print (Wg)
print (Qa, ca, Qb, cb)

print (palacze, "palacze")
print (grill, "grill")
print  (ulica, "ulica")