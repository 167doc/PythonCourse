"""
dny = [
    "Pondělí",
    "Úterý",
    "Středa",
    "Čtvrtek",
    "Pátek",
    "Sobota",
    "Neděle"
]

cislo = int(input("Zadej číslo dne: "))
if 0<cislo<7:
    print(dny[cislo - 1])
else:
    print(Nespravny den)


text = input("Zadej text: ")    #Вывести текст наоборот с помощью цикла

obracene = ""

for znak in text:
    obracene = znak + obracene

print(obracene)



platy = input("Zadej platy oddělené čárkou: ")  #Среднее значение зарплат

platy = platy.split(",")

soucet = 0

for plat in platy:
    plat = int(plat.strip())
    soucet += plat

prumer = soucet / len(platy)

print("Průměrný plat:", prumer)
"""

text = input("Zadej text: ")   #Сумма всех цифр в произвольном тексте

soucet = 0

for znak in text:
    if ord(znak) >= 48 and ord(znak) <= 57:
        soucet += (ord(znak) - 48)

print("Součet číslic:", soucet)

