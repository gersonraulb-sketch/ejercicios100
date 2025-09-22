gerson = ["rojo", "azul", "rojo", "verde", "rojo"]
raul = input("Ingrese un color: ")

if raul in gerson:
    print(f"El color esta {gerson.count(raul)} veces en la lista")
else:
    print("No esta en la lista")
