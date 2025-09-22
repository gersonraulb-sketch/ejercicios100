gerson = {"dog": "perro", "cat": "gato",
          "house": "casa", "car": "carro", "tree": "árbol"}
print("Palabras:")
for raul, botia in gerson.items():
    print(f"{raul}")

rodriguez = input("Ingrese una palabra en inglés: ").lower()
if rodriguez in gerson:
    print(f"La traducción de {rodriguez} es {gerson[rodriguez]}")
else:
    print("Palabra no encontrada")
