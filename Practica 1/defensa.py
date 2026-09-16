class Temperatura:
    def __init__(self, valor, unidad):
        self.valor = valor
        self.unidad = unidad.upper()
        
    def convertir(self, nueva_unidad):
        nueva_unidad = nueva_unidad.upper()
        if self.unidad == "F":
            celsius = (self.valor - 32) * (5.0 / 9.0)
        elif self.unidad == "K":
            celsius = self.valor - 273.15
        else:
            celsius = self.valor
            
        if nueva_unidad == "F":
            resultado = (celsius * (9.0 / 5.0)) + 32
        elif nueva_unidad == "K":
            resultado = celsius + 273.15
        else:
            resultado = celsius
            
        self.valor = resultado
        self.unidad = nueva_unidad
        return self.valor
    
if __name__ == "__main__":
    temp1 = 30.2
    unidad_temp1 = "C"
    t1 = Temperatura(temp1, unidad_temp1)
    print(f"Termómetro 1: {t1.valor} °{t1.unidad}")
    temp2 = 40.2
    unidad_temp2 = "F"
    t2 = Temperatura(temp2, unidad_temp2)
    print(f"Termómetro 2: {t2.valor} °{t2.unidad}")
    t2.convertir("C")
    print(f"Termómetro 2: {t2.valor:.2f} °{t2.unidad}")