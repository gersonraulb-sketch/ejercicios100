gerson = [2, 4, 6]
botia = [1, 3, 5]

raul = int(input("Ingrese un número: "))

if raul in gerson or raul in botia:
    print("El número está en alguna de las listas")
else:
    print("El número no está en ninguna lista")
