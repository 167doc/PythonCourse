def pozdrav():
    print("Hurá")


for i in range(3):
    pozdrav()


def nazev_dne(index):
    dny = ["Pondělí", "Úterý", "Středa",
           "Čtvrtek", "Pátek", "Sobota", "Neděle"]

    if index >= 1 and index <= 7:
        return dny[index - 1]

    return "Neplatný den"


index = int(input("Zadej číslo dne (1-7): "))

print(nazev_dne(index))