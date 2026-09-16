class AlgebraVectorial:
    def perp_1(self, a, b):
        return round(abs(a + b), 5) == round(abs(a - b), 5)

    def perp_2(self, a, b):
        return round(abs(a - b), 5) == round(abs(b - a), 5)

    def perp_3(self, a, b):
        return (a * b) == 0

    def perp_4(self, a, b):
        return round(abs(a + b)**2, 5) == round(abs(a)**2 + abs(b)**2, 5)

    def paralela_1(self, a, b, r):
        return a == (b * r)

    def paralela_2(self, a, b):
        c = a.cruz(b)
        return c.a1 == 0 and c.a2 == 0 and c.a3 == 0

    def proyeccion(self, a, b):
        return b * ((a * b) / (abs(b)**2))

    def componente(self, a, b):
        return (a * b) / abs(b)