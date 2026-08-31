"""
for i in range(3):
    print("Hello World")

for i in range(1,11):
    print(i)

for i in range(10,0,-1):
    print(i)
"""

pismena = "ABCDEFGH"

print("  " + " ".join(pismena))

for i in range(8, 0, -1):
    print(i, end=" ")

    for j in range(8):
        if (i + j) % 2 == 0:
            print("#", end=" ")
        else:
            print(" ", end=" ")

    print()

