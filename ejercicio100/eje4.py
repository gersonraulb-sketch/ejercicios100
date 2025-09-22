gerson = ["Carro", "Moto", "Bicicleta"]
print(f"Vehiculos disponibles: {gerson}")

raul = input("Eliga un vehiculo de la lista, o ingrese uno nuevo: ").title()

if raul in gerson:
    print(f"Elegiste {raul}")
else:
    gerson.append(raul)
    print(f"Elegiste {raul}, ahora la lista es {gerson}")
