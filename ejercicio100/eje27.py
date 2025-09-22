gerson = (("Pizza", 15000), ("Hamburguesa", 12000), ("Perro caliente", 8000))

print("Menú disponible:")
for i, (raul, botia) in enumerate(gerson):
    print(f"{i} - {raul}: ${botia}")

rodriguez = int(input("Seleccione lo que desea ordenar: "))

print(
    f"Ha ordenado {gerson[rodriguez][0]} debe pagar: ${gerson[rodriguez][1]}")
