import math

class Estadistica:
    def __init__(self, datos):
        self.__datos = datos

    def promedio(self):
        return sum(self.__datos) / len(self.__datos)

    def desviacion(self):
        prom = self.promedio()
        suma = sum((x - prom) ** 2 for x in self.__datos)
        return math.sqrt(suma / (len(self.__datos) - 1))

# Programa de prueba
datos = list(map(float, input("Ingrese los 10 números: ").split()))
est = Estadistica(datos)
print(f"El promedio es {est.promedio():.2f}")
print(f"La desviación estandard es {est.desviacion():.5f}")