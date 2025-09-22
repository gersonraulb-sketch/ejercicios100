gerson = ["manzana", "banana", "cereza"]
print(f"Tenemos {gerson}")

raul = input("Eliga una fruta para su jugo: ")

if raul in gerson:
    print(f"Aqui tiene su juego de {raul}")
else:
    print("No tenemos esa fruta")
