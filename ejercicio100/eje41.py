gerson = {"Ana": "Presente", "Raul": "Ausente", "Luis": "Presente"}

raul = input("Ingrese nombre del estudiante: ")

if raul in gerson:
    print(f"{raul} está marcado como {gerson[raul]}")
else:
    print("No se encuentra en la lista")
