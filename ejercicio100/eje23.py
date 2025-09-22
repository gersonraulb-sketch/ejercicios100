gerson = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
print(f"Tupla completa: {gerson}")

raul = int(input("Ingrese de que letra desea partir (0 a 7): "))
botia = int(input("Ingrese hasta cual desea llegar(1 a 8): "))

rodriguez = gerson[raul:botia]

print(f"las letras entre {raul} y {botia}: {rodriguez}")
