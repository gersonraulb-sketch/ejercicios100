gerson = {"Carlos": 50000, "Ana": 100000}

raul = input("Ingrese su nombre: ")

if raul in gerson:
    botia = int(input("Ingrese cantidad a retirar: "))
    if botia <= gerson[raul]:
        gerson[raul] -= botia
        print(f"Retiro exitoso. Saldo restante: {gerson[raul]}")
    else:
        print("Fondos insuficientes")
else:
    print("Usuario no encontrado")
