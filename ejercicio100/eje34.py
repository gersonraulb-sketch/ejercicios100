gerson = {"carol": "1234", "raul": "abcd"}

raul = input("Ingrese su usuario: ")
botia = input("Ingrese su contraseña: ")

if gerson.get(raul) == botia:
    print("Acceso permitido")
else:
    print("Usuario o clave incorrectos")
