gerson = ["Camilo", "Ana", "Luis"]


print(f"Participantes disponibles: {gerson}")
raul = input("Eliga un participante: ").title()

if raul in gerson:
    print(f"Elegiste a {raul}")
else:
    print("El participante no está en la lista")
