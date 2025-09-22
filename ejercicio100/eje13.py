gerson = ["pera", "manzana"]
raul = ["uva", "mango"]

botia = input("¿Quiere combinar las dos listas? (si/no): ").lower()

if botia == "si":
    rodriguez = gerson + raul
    print(rodriguez)
else:
    print(f"Lista 1: {gerson} y Lista 2: {raul}")
