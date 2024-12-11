import math
class AceleracionTangencial():
	def __init__(self):
		self.pi = math.pi

	def Ac1(self, vt, r):
		Ac = (vt**2)/r
		return Ac
		
	def r1(self, vt, ac):
		r = (vt**2)/ac
		return r
	def vt(self, ac, r):
		vt = (r*ac)**.5
		return vt

	def Ac2(self, w, r):
		Ac = (w**2)*r
		return Ac

	def w(self, r, ac):
		w = (ac/r)**.5
		return w

	def r2(self, ac, w):
		r = ac/w**2
		return r

	def Ac3(self, f, r):
		Ac = ((2*self.pi*f)**2)*r
		return Ac

	def r3(self, f, ac):
		r = ac/((2*self.pi*f)**2)
		return r

	def f(self, r, ac):
		f = (((ac/r)**.5)/self.pi)/2
		return f

	def Ac4(self, t, r):
		Ac = (((2*self.pi)/t)**2)*r
		return Ac

	def t(self, ac, r):
		t = (2*self.pi)/(ac/r)**.5
		return t

	def r4(self, t, ac):
		r = ac/(((2*self.pi)/t)**2)
		return r

	def fcen(self, m, ac):
		fcen = m*ac
		return fcen

	def m(self, ac, fcen):
		m = fcen/ac
		return m
		
	def ac5(self, m, fcen):
		ac = fcen/m
		return ac
