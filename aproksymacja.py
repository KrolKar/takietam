import numpy as np
import matplotlib.pyplot as plt
import math as m
import scipy.optimize


# -------------------------------------------------------------------------------------
def read_data():

    lines = [line.rstrip('\n') for line in open('data8.txt')]

    wartosci = []
    czas = []
    odp_skok = []

    for line in lines:
        czas.append(line.split()[0])
        odp_skok.append(line.split()[1])



    plt.plot(czas, odp_skok, 'bx')
    plt.plot(czas, odp_skok, 'b')
    return wartosci, czas, odp_skok

def odpSkok(t, tau, tauz, k, dzeta):
    if dzeta >= 1:
        return 10000
    if dzeta < -1:
        return 10000
    if tau < 0.01:
        return 10000
    return k * (
        tauz * 1 / (tau * m.sqrt(1 - dzeta ** 2)) * m.exp(-dzeta * t / tau) * m.sin(t * m.sqrt(1 - dzeta ** 2) / tau) + (
        1 - m.exp(-dzeta * t / tau) / m.sqrt(1 - dzeta ** 2) * m.sin(t * m.sqrt(1 - dzeta ** 2) / tau + m.acos(dzeta))))

def funk(parm):
    k = 0
    for i in range(len(odp_skok)):
        k += (float(odp_skok[i]) - odpSkok(float(czas[i]), *parm)) ** 2
    return k

def odpUkladu():
    odp = []
    pod = []
    param = scipy.optimize.fmin(funk, (1, -1, 1, 0.75))
    #param[2] = param[2] - 2
    print(param)
    for i in range(120):
        odp.append(odpSkok(float(i)/10, *param))
        pod.append(float(i)/10)

    plt.plot(pod, odp, 'r')



# -------------------------------------------------------------------------------------
wartosci, czas, odp_skok = read_data()
funk((1, -1, 1, 0.75))
odpUkladu()


plt.show()