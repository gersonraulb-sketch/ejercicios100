gerson = {"gatos": 0, "perros": 0, "wonka": 0}

print("Encuesta: ¿Cuál prefieres?")
for opcion in gerson:
    print(opcion)

raul = input("Elija su opción: ")
if raul in gerson:
    gerson[raul] += 1

print("Resultados:", gerson)
