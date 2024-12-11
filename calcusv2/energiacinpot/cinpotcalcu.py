class Energy:
    def __init__(self, name):
        self.name = name
        self.logo = "lavine.png"

    def massv1(self, ep, g, h):
        m = ep/g/h
        return m

    def massv2(self, ec, v):
        m = ec/v**2/2
        return m

    def height(self, ep, g, m):
        h = ep/g/m
        return h

    def velocity(self, ec, m):
        v = (ec*2/m)**.5
        return v

    def ecin(self, m, v):
        ec = m * v**2 /2
        return ec

    def epot(self, m, h, g):
        ep = m*h*g
        return ep

    def gravity(self, ep, h, m):
        g = ep/h/m
        return g