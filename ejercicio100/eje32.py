gerson = {"pan": 3000, "leche": 5000, "huevos": 12000}

print("Inventario actual:", gerson)
raul = input("¿Qué producto quiere comprar?: ")

if raul in gerson:
    print(f"El precio de {raul} es ${gerson[raul]}")
else:
    print("Producto no disponible")
