gerson = {"A": "Excelente", "B": "Bueno",
          "C": "Aceptable", "D": "Deficiente", "F": "Reprobado"}

raul = input("Ingrese su calificación (A-F): ")
print(f"Resultado: {gerson.get(raul.upper(), 'Calificación no válida')}")
