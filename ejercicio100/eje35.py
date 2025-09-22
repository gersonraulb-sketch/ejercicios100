gerson = {"pizza": 15000, "hamburguesa": 12000, "ensalada": 10000}

print("Menú:")
for raul, botia in gerson.items():
    print(f"{raul}: ${botia}")

rodriguez = input("Ingrese un plato del memú: ").lower().split(",")
totalgerson = sum(gerson.get(items.strip(), 0) for items in rodriguez)

print(f"El total es: ${totalgerson}")
