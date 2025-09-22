gerson = (("Mamá", "3214567890"), ("Amigo", "3109876543"))

print("Contactos guardados:")
for i, (botia, rodriguez) in enumerate(gerson):
    print(f"{i}: {botia}")

raul = int(input("Elija un número de contacto: "))
print(f"El número de tu {gerson[raul][0]} es {gerson[raul][1]}")
