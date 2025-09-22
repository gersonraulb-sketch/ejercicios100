def sistema(estudiante, notas):
    gerson = sum(notas) / len(notas)
    estado = "Aprobado" if gerson >= 3.0 else "Reprobado"
    print(
        f"Estudiante: {estudiante}\nNotas: {notas}\nPromedio: {gerson:.2f}\nEstado: {estado}")


botia = input("Ingrese el nombre del estudiante: ")
rodriguez = [float(x) for x in input(
    "Ingrese sus notas (1,2): ").split(",")]
sistema(botia, rodriguez)
