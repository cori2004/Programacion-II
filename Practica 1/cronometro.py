import time
import random

class Cronometro:
    def __init__(self):
        self.__inicia = time.time() * 1000
        self.__finaliza = 0.0

    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = time.time() * 1000

    def detener(self):
        self.__finaliza = time.time() * 1000

    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia

# Mi programa de prueba
def ordenacionSeleccion(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Usamos 3000 para que no se muera tu compu, cámbialo a 100000 si quieres sufrir xd
lista = [random.randint(1, 1000) for _ in range(3000)]

c = Cronometro()
c.inicia()
ordenacionSeleccion(lista)
c.detener()

print("Tiempo transcurrido:", c.lapsoDeTiempo(), "milisegundos")