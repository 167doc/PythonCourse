import copy as cp
class Kostka():
    #game dice

    def __init__(self,pocet_sten=6):
        self.__pocet_sten=pocet_sten

    def vrat_pocet_sten(self):
        return self.__pocet_sten # Python name mangling: _Kostka__pocet_sten

    def hod(self):
        #returns numbers from 1 to number of sides of the dice 
        import random as _random
        return _random.randint(1, self.__pocet_sten)

    def __str__(self):
        """
        Vrací textovou reprezentaci kostky.
        """
        return str(f"Kostka s {self.__pocet_sten} stěnami.")

class Hrac():
    def __init__(self, jmeno, kostka):
        self.jmeno = jmeno
        self.kostka = kostka
    def __str__(self):
        return f"{self.jmeno}:{self.kostka}"   


"""
kopie_hrace = cp.copy(hrac)

# Změníme původní kostku
kostka._pocet_sten = 8

print(hrac)
print(kopie_hrace)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
"""
kostka = Kostka(6)
hrac = Hrac("Pavel", kostka)

# Vytvoříme hlubokou kopii hráče
kopie_hrace = cp.deepcopy(hrac)
# Změníme původní kostku
kostka._Kostka__pocet_sten = 8
print(hrac)
print(kopie_hrace)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

"""
# Vytvoříme instanci kostky s 6 stěnami
moje_kostka = Kostka(6)
print(f"Constuctor method - original:{moje_kostka}")

# Vytvoříme kopii instance moje_kostka pomocí konstruktoru
kopie_kostky = Kostka(moje_kostka.vrat_pocet_sten())
print(f"Constuctor method - copy:{kopie_kostky}")

import copy as cp

# Vytvoříme instanci kostky s 6 stěnami
puvodni_kostka = Kostka(6)
print(f"Copy method - original:{puvodni_kostka}")

# Vytvoříme mělkou kopii instance puvodni_kostka
melka_kopie_kostky = cp.copy(puvodni_kostka)
print(f"Copy method - copy:{melka_kopie_kostky}")

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# vytvoření kostek
sestistenna = Kostka()
desetistenna = Kostka(10)

#hod šestistěnnou
print(sestistenna)
for _ in range(6):
    print(sestistenna.hod(), end=" ")

#hod desetistěnnou
print("\n", desetistenna, sep=" ")
for _ in range(10):
    print(desetistenna.hod(), end=" ")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
desetistenna = Kostka(10)
print(f"Před pokusem o úpravu privátního atributu: {desetistenna}")
desetistenna.__pocet_sten = 365
print(f"Upravili jsme atribut na hodnotu: {desetistenna.__pocet_sten}")
print(f"Po pokusu o úpravu privátního atributu: {desetistenna}")

desetistenna._Kostka__pocet_sten = 365
print(desetistenna)
"""