import random


def adivinar():
    gerson = random.randint(1, 20)
    raul = 0
    while True:
        raul = int(input("Adivina el número (1-20): "))
        raul += 1
        if raul == gerson:
            print(f"Bien, Lo lograste en {raul} intentos")
            break
        elif raul < gerson:
            print("Muy bajo")
        else:
            print("Muy alto")


adivinar()
