def votar():
    gerson = {"a": 0, "b": 0, "c": 0}
    while True:
        raul = input("Ingrese su voto (a, b, c). 0 para salir: ")
        if raul == "0":
            break
        elif raul in gerson:
            gerson[raul] += 1
        else:
            print("Invalido")

    print("Resultados:", gerson)


votar()
