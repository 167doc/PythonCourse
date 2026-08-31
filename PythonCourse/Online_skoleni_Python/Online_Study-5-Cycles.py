"""for i in range(3):
    print(f"Hura po {i}")

j=0
while j<3:
     print(f"Hura po {j+1}")
     j=j+1
"""
print("Mala nasobilka pomoci dvou cyklu")
for j in range(1,11):
    for i in range (1,11):
        print(f"|{i*j}| \t", end="")
    print()