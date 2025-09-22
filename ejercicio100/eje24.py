gerson = (10, 20, 30)

x, y, z = gerson

print(f"Coordenada X: {x}")
print(f"Coordenada Y: {y}")
print(f"Coordenada Z: {z}")

raul = int(input("¿Cuánto quiere mover en X?: "))
botia = int(input("¿Cuánto quiere mover en Y?: "))
rodriguez = int(input("¿Cuánto quiere mover en Z?: "))

nuevas_coordenadas = (x + raul, y + botia, z + rodriguez)

print(f"Nueva posición en 3D: {nuevas_coordenadas}")
