import math

a=float(input("Zadej cislo: "))
if a>0:
    odmocnina=math.sqrt(a)
    print(f"Odmocnina z cisla {a} je {odmocnina}")
else:
    print("Odmocnina ze zapornejo cisla neexistuje")