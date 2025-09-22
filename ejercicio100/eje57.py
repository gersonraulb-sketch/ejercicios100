def propina(cuenta, porcentaje):
    gerson = cuenta * (porcentaje / 100)
    return gerson


raul = float(input("Ingrese su cuenta: "))
botia = float(input("Ingrese el porcentaje de propina: "))

print(f"La propina es de: {propina(raul, botia)}")
