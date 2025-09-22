def cajero(usuario, raul):
    print(f"Bienvenido {usuario}, tu saldo es ${raul}")
    gerson = int(input("¿Cuánto deseas retirar?: "))
    if gerson <= raul:
        raul -= gerson
        print(f"Retiro exitoso, tu nuevo saldo es ${raul}")
    else:
        print("Fondos insuficientes")


cajero("Camilo", 100000)
