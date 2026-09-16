import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)

    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b + math.sqrt(disc)) / (2 * self.__a)

    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b - math.sqrt(disc)) / (2 * self.__a)

# Programa de prueba
a, b, c = map(float, input("Ingrese a, b, c: ").split())
ec = EcuacionCuadratica(a, b, c)
disc = ec.getDiscriminante()

if disc > 0:
    print(f"La ecuación tiene dos raíces {ec.getRaiz1()} y {ec.getRaiz2()}")
elif disc == 0:
    print(f"La ecuación tiene una raíz {ec.getRaiz1()}")
else:
    print("La ecuación no tiene raíces reales")