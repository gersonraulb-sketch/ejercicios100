gerson = (("perro", "gato"), ("helado", "perro caliente"), ("carro", "moto"))
print("0 = animales, 1 = comida, 2 = vehículos")

raul = int(input("¿Que grupo quiere ver?: "))
print(f"contenido: {gerson[raul]}")

botia = int(input("Elija que desea quedarse (0-1): "))
print(f"Ahora {gerson[raul][botia]} es suyo")
