import numpy as np

class Krawedz:
    def __init__(self, koszt, cel):
        self.koszt = koszt
        self.cel = cel

class Wezel:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.sasiedzi = []

    def dodajKrawedz(self, koszt, cel):
        krawedz = Krawedz(koszt, cel)
        self.sasiedzi.append(krawedz)

def dijkstra(graf, start, stop):
    rozmiar = len(graf)
    DUZO = 1000
    otwarta = np.zeros(rozmiar)
    zamknieta = np.zeros(rozmiar)
    rodzic = np.zeros(rozmiar)
    otwarta.fill(DUZO)
    zamknieta.fill(DUZO)
    rodzic.fill(DUZO)
    otwarta[start] = 0
    rodzic[start] = -1

    while zamknieta[stop] == DUZO:
        najtanszy = otwarta.argmin()
        print(najtanszy)
        if otwarta[najtanszy] == DUZO:
            return None
        else:
            zamknieta[najtanszy] = otwarta[najtanszy]
            otwarta[najtanszy] = DUZO
            for krawedz in graf[najtanszy].sasiedzi:
                cel = krawedz.cel
                koszt = krawedz.koszt
                nowyKoszt = zamknieta[najtanszy] + koszt
                if nowyKoszt <= otwarta[cel] and zamknieta[cel] == DUZO:
                    otwarta[cel] = nowyKoszt
                    rodzic[cel] = najtanszy
    droga = []
    obecny = stop
    while obecny != start:
        droga.append(obecny)
        obecny = int(rodzic[obecny])
    droga.append(obecny)
    droga.reverse()
    return droga

def switch (n):
    return {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G'
    }[n]

if __name__=="__main__":
    graf = []
    wezel0 = Wezel(0)
    wezel0.dodajKrawedz(6, 2)
    wezel0.dodajKrawedz(2, 3)
    graf.append(wezel0)
    wezel1 = Wezel(1)
    wezel1.dodajKrawedz(2, 2)
    wezel1.dodajKrawedz(3, 5)
    graf.append(wezel1)
    wezel2 = Wezel(2)
    wezel2.dodajKrawedz(6, 0)
    wezel2.dodajKrawedz(2, 1)
    wezel2.dodajKrawedz(1, 3)
    wezel2.dodajKrawedz(3, 4)
    graf.append(wezel2)
    wezel3 = Wezel(3)
    wezel3.dodajKrawedz(2, 0)
    wezel3.dodajKrawedz(1, 2)
    wezel3.dodajKrawedz(1, 6)
    graf.append(wezel3)
    wezel4 = Wezel(4)
    wezel4.dodajKrawedz(3, 2)
    wezel4.dodajKrawedz(2, 5)
    graf.append(wezel4)
    wezel5 = Wezel(5)
    wezel5.dodajKrawedz(3, 1)
    wezel5.dodajKrawedz(2, 4)
    wezel5.dodajKrawedz(1, 6)
    graf.append(wezel5)
    wezel6 = Wezel(6)
    wezel6.dodajKrawedz(1, 3)
    wezel6.dodajKrawedz(1, 5)
    graf.append(wezel6)
    droga = dijkstra(graf, 0, 5)
    sciezka = []
    for wezel in droga:
        sciezka.append(switch(wezel))
    print("droga: ", sciezka)
