class Cargas:
    def __init__(self, name):
        self.k = 8.9875517873681764*10**9
        self.name = name

    def q1(self, q2, d, f):
        q2 *= 1e-6
        q1 = (f * d**2) / (self.k * q2)
        return q1

    def q2(self, q1, d, f):
        q1 *= 1e-6
        q2 = (f * d**2) / (self.k * q1)
        return q2

    def d(self, q1, q2, f):
        q1 *= 1e-6
        q2 *= 1e-6
        d = (self.k * ((q1 * q2) / f))**.5
        return d

    def f(self, q1, q2, d):
        q1 *= 1e-6
        q2 *= 1e-6
        f = self.k * ((q1 * q2) / d**2)
        return f

               
