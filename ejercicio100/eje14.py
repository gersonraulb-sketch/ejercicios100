gerson = []
while len(gerson) < 5:
    raul = int(input("Ingrese algunos numeros: "))
    gerson.append(raul)

print(f"Lista original: {gerson}")

gerson.sort()
print(f"Lista ordenada: {gerson}")
