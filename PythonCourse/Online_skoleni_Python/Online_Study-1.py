vstup=" C++ je [kolikrat] KRAT lepsi! "

vstup=vstup.strip().lower()
print(vstup)

vstup=vstup.replace("c++ ","Python ")
print(vstup)
print(f"Zacina se 'Python': {vstup.startswith("Python ")}")
print("krat" in vstup)
print(vstup.replace("[kolikrat]", str(len(vstup) * 3)))