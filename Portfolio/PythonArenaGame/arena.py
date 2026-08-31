#!/usr/bin/env python3

class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def _vykresli(self):
       # zakomentováno kvůli kompileru
        self._vycisti_obrazovku()
        print("-------------- Aréna -------------- \n")
        print("Zdraví bojovníků: \n")
        print(f"{self._bojovnik_1} {self._bojovnik_1.graficky_zivot()}")
        print(f"{self._bojovnik_2} {self._bojovnik_2.graficky_zivot()}")


    def _vycisti_obrazovku(self):
        import os as _os
        _os.system('cls' if _os.name == 'nt' else 'clear')
    
    def _vypis_zpravu(self, zprava):
        import time as _time
        print(zprava)
        # zakomentováno kvůli kompileru
        _time.sleep(1.5)

    def zapas(self):
        import random as _random
        print("Vítejte v aréně!")
        print(f"Dnes se utkají {self._bojovnik_1} a {self._bojovnik_2}!")
        print("Zápas může začít...", end=" ")
        input()

        # prohození bojovníků
        if _random.randint(0, 1):
            (self._bojovnik_1, self._bojovnik_2) = (self._bojovnik_2,
                                                    self._bojovnik_1)
        # cyklus s bojem
        while self._bojovnik_1.je_nazivu() and self._bojovnik_2.je_nazivu():
            self._bojovnik_1.utoc(self._bojovnik_2)
            self._vykresli()
            self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())
            self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
            if self._bojovnik_2.je_nazivu():
                self._bojovnik_2.utoc(self._bojovnik_1)
                self._vykresli()
                self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
                self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())

