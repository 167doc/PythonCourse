class Uzivatel:
    def __init__(self, jmeno, heslo, vek):
        self._jmeno=jmeno
        self._heslo=heslo
        self._vek=vek

    def prihlasitse(self, heslo):
        pass

    def odhlasit(self):
        pass

    def nastavit_vahu(self, zvire):
        pass

#class TridaPotomka(TridaRodice):

class Administrator(Uzivatel):
    def __init__(self, jmeno, heslo, vek, telefonni_cislo):
       super().__init__(jmeno,heslo, vek)
       self.telefonni_cislo=telefonni_cislo


    def pridat_zvire(self, zvire):
        pass

    def vymaz_zvire (self, zvire):
        pass

        