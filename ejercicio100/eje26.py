gerson = ("perro", "hipopotamo", "gato", "elefante")
raul = input(
    "¿Quiere saber cual es la palabra mas larga o la mas corta? (1/2): ")

if raul == "1":
    print(f"La palabra más larga es: {max(gerson, key=len)}")
elif raul == "2":
    print(f"La palabra más corta es: {min(gerson, key=len)}")
