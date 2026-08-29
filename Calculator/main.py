from Calculator_OOP import Calculator


kalkulacka=Calculator()
a = float(input("Zadej 1. číslo: "))
kalkulacka.a = a
b = float(input("Zadej 2. číslo: "))
kalkulacka.b = b
print(f"Součet: {kalkulacka.addition()}")
print(f"Rozdíl: {kalkulacka.substraction()}")
print(f"Součin: {kalkulacka.multiply()}")
print(f"Podíl: {kalkulacka.divide()}")
