def traductor(palabra):
    gerson = {
        "perro": {"en": "dog", "fr": "chien"},
        "gato": {"en": "cat", "fr": "chat"},
        "casa": {"en": "house", "fr": "maison"}
    }

    if palabra in gerson:
        print(
            f"Inglés: {gerson[palabra]["en"]}, Francés: {gerson[palabra]["fr"]}")
    else:
        print("Palabra no encontrada")


raul = input("Ingrese una palabra en español (perro, gato, casa): ")

traductor(raul)
