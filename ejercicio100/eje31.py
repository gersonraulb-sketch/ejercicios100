gerson = {"Mamá": "3214567890", "Amigo": "3109876543"}

print("Contactos guardados:")
for raul in gerson:
    print(raul)

botia = input("¿Desea agregar un contacto? (si/no):")
if botia.lower() == "si":
    nombre = input("Ingrese el nombre: ")
    tel = input("Ingrese el número: ")
    gerson[nombre] = tel
    print("Contacto agregado.")
    print(f"Contactos: {list(gerson)}")
else:
    print("ok")
