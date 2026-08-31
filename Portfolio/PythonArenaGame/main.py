#!/usr/bin/env python3
from PythonCourse.OOP.TahovyBoj.kostka import Kostka
from PythonCourse.OOP.TahovyBoj.bojovnik import Bojovnik
from PythonCourse.OOP.TahovyBoj.arena import Arena
# vytvoření objektů
kostka = Kostka(10)
zalgoren = Bojovnik("Zalgoren", 100, 20, 10, kostka)
shadow = Bojovnik("Shadow", 60, 18, 15, kostka)
arena = Arena(zalgoren, shadow, kostka)
# zápas
arena.zapas()
