class Vehiculo:
    color = "negro"
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):
    velocidad = 180
    cilindrada = 2.0


auto1 = Coche()
print(auto1.puertas)
print(auto1.ruedas)
print(auto1.velocidad)
print(auto1.color)
