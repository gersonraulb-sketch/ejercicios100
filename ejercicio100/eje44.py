gerson = {"Colombia": "Bogotá", "México": "Ciudad de México",
          "Argentina": "Buenos Aires"}

raul = input("Ingrese un país: ")
print(f"La capital de {raul} es {gerson.get(raul, 'No registrada')}")
