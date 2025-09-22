gerson = []

while len(gerson) < 2:
    raul = int(input("Ingrese dos numeros para sumarlos: "))
    gerson.append(raul)

botia = sum(gerson)
print(f"La suma de {gerson} es {botia}")
