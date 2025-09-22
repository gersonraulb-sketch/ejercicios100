import random


def dado():
    return random.randint(1, 6)


input("Presione el enter para tirar el dado ")
print(f"Salio {dado()}")
