class Osoba:
    """Reprezentuje jednu osobu v rodokmenu."""

    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.otec = None
        self.matka = None
        self.deti = []

    def nastav_rodice(self, otec=None, matka=None):
        """Nastaví otce a matku osoby."""
        self.otec = otec
        self.matka = matka

        if otec and self not in otec.deti:
            otec.deti.append(self)

        if matka and self not in matka.deti:
            matka.deti.append(self)

    def vypis_rodice(self):
        """Vypíše rodiče osoby."""
        print(f"\nRodiče osoby {self.jmeno}:")

        print(f"Otec: {self.otec.jmeno if self.otec else 'neuveden'}")
        print(f"Matka: {self.matka.jmeno if self.matka else 'neuvedena'}")

    def vypis_deti(self):
        """Vypíše děti osoby."""
        print(f"\nDěti osoby {self.jmeno}:")

        if not self.deti:
            print("Žádné děti.")
            return

        for dite in self.deti:
            print(f"- {dite.jmeno}")

    def __str__(self):
        return self.jmeno