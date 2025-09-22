gerson = {"USD": 4000, "EUR": 4500, "MXN": 220}

print("Monedas disponibles:", list(gerson.keys()))
raul = input("Ingrese la moneda a convertir(USD, EUR, MXN): ")
botia = float(input("Ingrese cantidad: "))

if raul in gerson:
    print(f"{botia} {raul} = {botia * gerson[raul]} COP")
else:
    print("Divisa no válida")
