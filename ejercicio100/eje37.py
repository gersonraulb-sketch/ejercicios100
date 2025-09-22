gerson = {"Ana": 4.0, "Raul": 3.2, "Luis": 4.5}

print("Estudiantes:", list(gerson.keys()))
raul = input("Ingrese el nombre del estudiante: ").title()

if raul in gerson:
    print(f"{raul} tiene una nota de {gerson[raul]}")
else:
    print("Estudiante no registrado")
