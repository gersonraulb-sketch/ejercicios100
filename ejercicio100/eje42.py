gerson = {"Arroz": 25, "Frijoles": 40, "Aceite": 15}

print("Stock disponible:", gerson)
raul = input("Ingrese un producto: ")

if raul in gerson:
    botia = int(input("¿Cuántas unidades desea?: "))
    if botia <= gerson[raul]:
        gerson[raul] -= botia
        print(f"Compra realizada. Stock restante de {raul}: {gerson[raul]}")
    else:
        print("No hay suficiente stock")
else:
    print("Producto no encontrado")
