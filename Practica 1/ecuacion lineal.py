class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0

    def getX(self):
        denominador = self.__a * self.__d - self.__b * self.__c
        if denominador == 0:
            return 0
        return (self.__e * self.__d - self.__b * self.__f) / denominador

    def getY(self):
        denominador = self.__a * self.__d - self.__b * self.__c
        if denominador == 0:
            return 0
        return (self.__a * self.__f - self.__e * self.__c) / denominador

# Programa de prueba
a, b, c, d, e, f = map(float, input("Ingrese a, b, c, d, e, f: ").split())
eq = EcuacionLineal(a, b, c, d, e, f)

if eq.tieneSolucion():
    print(f"x={eq.getX()}, y={eq.getY()}")
else:
    print("La ecuación no tiene solución")