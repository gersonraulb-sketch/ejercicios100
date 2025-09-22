gerson = ["futbol", "baloncesto", "tenis"]
print(f"Deportes disponibles: {gerson}")

raul = input("Eliga un deporte que desee eliminar o uno que desee agregar: ")
if raul in gerson:
    gerson.remove(raul)
    print(f"Lista actualizada: {gerson}")
else:
    gerson.append(raul)
    print(f"Lista actualizada: {gerson}")
