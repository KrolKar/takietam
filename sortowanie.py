# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:23:17 2017

@author: student
"""
from random import shuffle
import numpy as np
import time

def tablica(n):
    tab = [[i] for i in range(n)]
    shuffle(tab)
    return tab

def bombelkowy(tabl):
    tab = tabl[:]
    start = time.clock()
    zmiana = 1
    while zmiana == 1:
        zmiana = 0
        for i in range(len(tab)-1):
            if tab[i] > tab[i+1]:
                zmiana = 1
                buf = tab[i+1]
                tab[i+1] = tab[i]
                tab[i] = buf
                #break
    end = time.clock()
    print('bąbelkowa: ',end - start)
    #print(tab)
    
def sort(tabl):
    tab = tabl[:]
    start = time.clock()
    for i in range(len(tab)):
        indeks = i
        for j in range(i, len(tab)):
            if tab[indeks] > tab[j]:
                indeks = j
        tab[i], tab[indeks] = tab[indeks], tab[i]
    end = time.clock()
    print('sort: ', end - start)
    #print(tab)
    
def quickSort(tabl):
    tab = tabl[:]
    mniejsze = []
    rowne = []
    wieksze = []
    if len(tab) > 1:
        pivot = tab[0]
        for x in tab:
            if x < pivot:
                mniejsze.append(x)
            if x == pivot:
                rowne.append(x)
            if x > pivot:
                wieksze.append(x)
        return quickSort(mniejsze)+rowne+quickSort(wieksze) 
    else:  
        return tab
    

if __name__ == "__main__":
    tabl = tablica(1000)
    #print(tabl)
    bombelkowy(tabl)
    #print(tabl)
    sort(tabl)
    start = time.clock()
    tab = quickSort(tabl)
    end = time.clock()
    print('quicksort: ', end - start)
    #print(tab)
