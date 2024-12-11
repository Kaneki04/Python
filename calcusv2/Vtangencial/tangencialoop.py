import math
class VelocidadTanAN:
	def __init__(self, name):
		self.name = name
		self.pi = math.pi

	def velocidadAngular(self, f):
		w = 2*self.pi*f
		return w
		
	def velocidadAngular2(self, t):
		w = (2*self.p1)/t
		return w

	def velocidadTan1(self, r, t):
		vt = (2*self.pi*r)/t
		return vt

	def velocidadTan2(self, r, f):
		vt = 2*self.pi*r*f
		return vt

	def velocidadTan2(self, r, w):
		vt = r*w
		return vt

	def f(self, t):
		return 1/t

	def t(self, f):
		return 1/f
