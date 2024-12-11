class Calor:
    def __init__(self, name):
        # m1 *(ce1)*(rf-ti1) + m2* (ce2) *(tf-ti2)=0
        self.name = name

    def tf(self, m1, ce1, ti1, m2, ce2, ti2):
        tf = (((m1*ce1*ti1) + (m2*ce2*ti2)) / ((m1*ce1) + (m2*ce2)))
        return tf + 273.15

    def m1(self, ti1, ce1, m2, ce2, ti2, tf):
        m1 = -(m2*ce2*(tf - ti2))/(ce1*(tf-ti1))
        return m1

    def m2(self, m1, ti1, ce1, ce2, ti2, tf):
        m2 = -(m1*ce1*(tf - ti1))/(ce2*(tf-ti2))
        return m2

    def ce1(self, m1, ti1, m2, ce2, ti2, tf):
        ce1 = -(m2*ce2*(tf-ti2))/(m1*(tf-ti1))
        return ce1

    def ce2(self, m1, ce1, ti1, m2, ti2, tf):
        ce2 = -(m1*ce1*(tf-ti1))/(m2*(tf-ti2))
        return ce2

    def ti1(self, m1, ce1, m2, ti2, ce2, tf):
        ti1 = ((m2*ce2*(tf-ti2))/(m1*ce1)) + tf
        return ti1 + 273.15

    def ti2(self, m1, ce1, ti1, m2, ce2, tf):
        ti2 = ((m1*ce1*(tf-ti1))/(m2*ce2)) + tf
        return ti2 + 273.15





