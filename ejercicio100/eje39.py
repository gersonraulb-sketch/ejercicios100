gerson = {"Bogotá": "15°C", "Medellín": "22°C",
          "Cartagena": "30°C", "Mosquera": "25°C"}

raul = input("Ingrese su ciudad: ")
print(
    f"El clima en {raul} es {gerson.get(raul, '... No tengo datos de esa ciudad')}")
