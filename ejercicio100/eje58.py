import time


def cuenta_regresiva(segundos):
    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)
    print("BOOM💣")


raul = int(input("Ingrese segundos para la cuenta regresiva: "))
cuenta_regresiva(raul)
