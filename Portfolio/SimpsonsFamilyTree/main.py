import os

from osoba import Osoba
from rodokmen import Rodokmen


def vycisti_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Vytvoření rodokmenu
rodokmen = Rodokmen()

# Vytvoření osob
abraham = Osoba("Abraham Simpson")
penelope = Osoba("Penelope Olsen")

herb = Osoba("Herb Powers")
homer = Osoba("Homer Simpson")

pan_bouvier = Osoba("Pan Bouvier")
jackie = Osoba("Jackie Bouvier")

marge = Osoba("Marge Bouvier")
selma = Osoba("Selma Bouvier")

bart = Osoba("Bart Simpson")


# Nastavení rodičů
herb.nastav_rodice(abraham, penelope)
homer.nastav_rodice(abraham, penelope)

marge.nastav_rodice(pan_bouvier, jackie)
selma.nastav_rodice(pan_bouvier, jackie)

bart.nastav_rodice(homer, marge)


# Přidání osob do rodokmenu
for osoba in [
    abraham, penelope, herb, homer,
    pan_bouvier, jackie, marge, selma, bart
]:
    rodokmen.pridej_osobu(osoba)


# Výpis rodokmenu
vycisti_terminal()

print("========== RODOKMEN ==========")
print("\nRodokmen pro osobu Bart Simpson:\n")

rodokmen.vypis_rodokmen(bart)


# Vyhledání osoby
hledana_osoba = rodokmen.najdi_osobu("Homer Simpson")

if hledana_osoba:
    hledana_osoba.vypis_rodice()
    hledana_osoba.vypis_deti()