import math

def promedio(valores):
    return sum(valores) / len(valores)

def desviacion(valores):
    prom = promedio(valores)
    suma = sum((x - prom) ** 2 for x in valores)
    return math.sqrt(suma / (len(valores) - 1))

# Programa principal
datos = list(map(float, input("Ingrese los 10 números: ").split()))
print(f"El promedio es {promedio(datos):.2f}")
print(f"La desviación estandard es {desviacion(datos):.5f}")