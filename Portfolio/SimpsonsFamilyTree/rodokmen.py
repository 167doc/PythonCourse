class Rodokmen:
    """Spravuje osoby a vztahy v rodokmenu."""

    def __init__(self):
        self.osoby = []

    def pridej_osobu(self, osoba):
        """Přidá osobu do rodokmenu."""
        if osoba not in self.osoby:
            self.osoby.append(osoba)

    def najdi_osobu(self, jmeno):
        """Vyhledá osobu podle jména."""
        for osoba in self.osoby:
            if osoba.jmeno.lower() == jmeno.lower():
                return osoba

        return None

    def vypis_rodokmen(self, osoba, uroven=0):
        """Rekurzivně vypíše rodokmen osoby."""
        odsazeni = "    " * uroven

        print(f"{odsazeni}{osoba.jmeno}")

        if osoba.otec:
            print(f"{odsazeni}├── otec:")
            self.vypis_rodokmen(osoba.otec, uroven + 1)

        if osoba.matka:
            print(f"{odsazeni}└── matka:")
            self.vypis_rodokmen(osoba.matka, uroven + 1)