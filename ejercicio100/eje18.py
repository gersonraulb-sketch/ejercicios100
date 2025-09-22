gerson = ("pera", "uva", "mango", "kiwi", "piña")
print(f"Opciones: {gerson}")
raul = int(input("Elija un número (0-4): "))

if gerson[raul] == "mango":
    print("¡Eligió el mango, buena elección!")
else:
    print(f"Eligió: {gerson[raul]}")
