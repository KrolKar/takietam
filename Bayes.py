# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:27:52 2017

@author: student
"""

import matplotlib.pyplot as plt
import numpy as np

lines1 = [line.rstrip('\n') for line in open('data1.csv')]
x1 = []
y1 = []
lines1 = [line.replace(',','.') for line in lines1]
for line in lines1:
    x1.append(line.split('|')[0])
    y1.append(line.split('|')[1])
lines2 = [line.rstrip('\n') for line in open('data2.csv')]
x2 = []
y2 = []
lines2 = [line2.replace(',','.') for line2 in lines2]
for line in lines2:
    x2.append(line.split('|')[0])
    y2.append(line.split('|')[1])

#print(x1, y1)
#print(x2, y2)

x = 1
y = 1

liczbaCzerwonych = len(x1)
liczbaZielonych = len(x2)
liczbaWszystkich = liczbaZielonych + liczbaCzerwonych
aprioriCzerwonego = liczbaCzerwonych/liczbaWszystkich
aprioriZielonego = liczbaZielonych/liczbaWszystkich
#print(aprioriCzerwonego)
xWszystkie = x1 + x2
yWszystkie = y1 + y2
#print(xWszystkie)
dystanse = []
for i in range(len(xWszystkie)):
    r = np.sqrt(np.abs((x - float(xWszystkie[i]))**2 + (y - float(yWszystkie[i]))**2))
    dystanse.append(r)

odleglosci = dystanse[:]
odleglosci.sort()
#print(dystanse)
#print(odleglosci)
indeksy = []
zielone = 0
czerwone = 0
for i in range(4):
    for j in range(len(dystanse)):
        if odleglosci[i] == dystanse[j]:
            indeksy.append(j)
            if j < len(x1):
                czerwone += 1
            else:
                zielone += 1
            break
        
print(indeksy)

szansaZ = zielone/liczbaZielonych
szansaC = czerwone/liczbaCzerwonych

bZielone = aprioriZielonego * szansaZ
bCzerwone = aprioriCzerwonego * szansaC

print('zielone: ', bZielone)
print('czerwone: ', bCzerwone)

plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'go')
plt.plot(x, y, 'bo')
plt.show
