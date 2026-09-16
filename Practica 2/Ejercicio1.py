import math

class MiPunto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distancia(self, *args):
        if len(args) == 1:
            p = args[0]
            return math.sqrt((self.x - p.get_x())**2 + (self.y - p.get_y())**2)
        elif len(args) == 2:
            x2, y2 = args
            return math.sqrt((self.x - x2)**2 + (self.y - y2)**2)

p1 = MiPunto()
p2 = MiPunto(10, 30.5)
print(p1.distancia(p2))

p1 = MiPunto(0, 0)
p2 = MiPunto(10, 30.5)

d1 = p1.distancia(p2)
d2 = p1.distancia(10, 30.5)

print("Distancia usando el objeto MiPunto:", d1)
print("Distancia usando coordenadas sueltas:", d2)