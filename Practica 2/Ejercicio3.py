import math

class Vector3D:
    def __init__(self, a1=0, a2=0, a3=0):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def __add__(self, b):
        return Vector3D(self.a1 + b.a1, self.a2 + b.a2, self.a3 + b.a3)

    def __sub__(self, b):
        return Vector3D(self.a1 - b.a1, self.a2 - b.a2, self.a3 - b.a3)

    def __mul__(self, b):
        if isinstance(b, Vector3D):
            return self.a1 * b.a1 + self.a2 * b.a2 + self.a3 * b.a3
        return Vector3D(self.a1 * b, self.a2 * b, self.a3 * b)

    def __rmul__(self, b):
        return self.__mul__(b)

    def __abs__(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    def normal(self):
        lon = abs(self)
        return Vector3D(self.a1 / lon, self.a2 / lon, self.a3 / lon)

    def cruz(self, b):
        c1 = self.a2 * b.a3 - self.a3 * b.a2
        c2 = self.a3 * b.a1 - self.a1 * b.a3
        c3 = self.a1 * b.a2 - self.a2 * b.a1
        return Vector3D(c1, c2, c3)

    def __eq__(self, b):
        return self.a1 == b.a1 and self.a2 == b.a2 and self.a3 == b.a3