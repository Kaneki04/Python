from tkinter import *
from tkinter import messagebox
from tangencialoop import VelocidadTanAN 
from actanfcenoop import AceleracionTangencial
import pyperclip

calcuTan = VelocidadTanAN("Velocidad Tan/Ang/Ac")
calcuAc = AceleracionTangencial()
window = Tk()
window.config(padx=10, pady= 10)
window.title(calcuTan.name)

logo = PhotoImage(file="mcua.png")
canvas = Canvas(height=500, width=500)
canvas.create_image(250, 290, image=logo)
canvas.grid(column=0, row=0, columnspan=2, pady=10)

def calculate():
	w = float
	f = float
	t = float
	vt = float
	ac = float
	r = float
	fcen = float
	m = float
	values = []
	not_repeated_values = []
	box_dirty = []
	box = []
	try:
		if len(wEntry.get()) == 0 and len(pEntry.get()) != 0:
			f = float(pEntry.get())
			w = calcuTan.velocidadAngular(f)
			values.extend([w, f])
			box_dirty.append(f"V. Angular = {w}")

		if len(rEntry.get()) != 0 and len(vTanEntry.get()) == 0:
			r = float(rEntry.get())
			values.append(r)
			if len(tEntry.get()) != 0:
				t = float(tEntry.get())
				vt = calcuTan.velocidadTan1(r, t)
				values.extend([t,vt])
				box_dirty.append(f"V. Tangencial = {vt}")

			elif len(pEntry.get()) != 0:
				f = float(pEntry.get())
				vt = calcuTan.velocidadTan2(r, f)
				values.extend([f, vt])
				box_dirty.append(f"V. Tangencial = {vt}")

			elif len(wEntry.get()) != 0:
				w = float(wEntry.get())
				vt = calcuTan.velocidadTan3(r, w)
				values.extend([w,t])
				box_dirty.append(f"V. Tangencial = {vt}")

		if len(pEntry.get()) == 0 and len(tEntry.get()) != 0:
			t = float(tEntry.get())
			f = calcuTan.f(t)
			values.extend([t, f])
			box_dirty.append(f"Period = {f}")

		elif len(tEntry.get()) == 0 and len(pEntry.get()) != 0:
			f = float(pEntry.get())
			t = calcuTan.t(f)
			values.extend([f, t])
			box_dirty.append(f"Time = {t} s")

		if len(rEntry.get()) != 0:
			r = float(rEntry.get())
			values.append(r)

			if len(ActEntry.get()) != 0:
				ac = float(ActEntry.get())
				values.append(f"A. Tangencial = {ac}")

				if len(pEntry.get()) == 0:
					f = calcuAc.f(r, ac)
					values.append(f)
					box_dirty.append(f"Period = {f}")

				elif len(tEntry.get()) == 0:
					t = calcuAc.t(ac, r)
					values.append(t)
					box_dirty.append(f"Time = {t} s")

			if len(ActEntry.get()) != 0 and len(vTanEntry.get()) == 0:
				ac = float(ActEntry.get())
				vt = calcuAc.vt(ac, r)
				box_dirty.append(f"V. Tangencial = {vt}")
				values.extend([ac, vt])
				if len(wEntry.get()) == 0: 
					w = calcuAc.w(r, ac)
					values.append(w)
					box_dirty.append(f"V. Angular = {w} m/s")

			if len(ActEntry.get()) == 0:
				if len(wEntry.get()) != 0:
					w = float(wEntry.get)
					ac = calcuAc.Ac2(w, r)
					values.extend([w, ac])
					box_dirty.append(f"A. Tangencial = {ac}")

				elif len(vTanEntry.get()) != 0:
					vt = float(vTanEntry.get())
					ac = calcuAc.Ac1(vt, r)
					values.extend([vt, ac])
					box_dirty.append(f"A. Tangencial = {ac}")

					if len(wEntry.get()) == 0: 
						w = calcuAc.w(r, ac)
						values.append(w)
						box_dirty.append(f"V. Angular = {w} m/s")
					if len(pEntry.get()) == 0: 
						f = calcuAc.f(r, ac)
						values.append(f)
						box_dirty.append(f"Period = {f}")
					if len(tEntry.get()) == 0: 
						t = calcuAc.t(ac, r)
						values.append(t)
						box_dirty.append(f"Time = {t} s")

				elif len(pEntry.get()) != 0 and len(rEntry.get()):
					f = float(pEntry.get())
					ac = calcuAc.Ac3(f, r)
					values.extend([f, ac])
					box_dirty.append(f"A. Tangencial = {ac}")

				elif len(tEntry.get()) != 0:
					t = float(tEntry.get())
					ac = calcuAc.Ac4(t, r)
					values.extend([t, ac])
					box_dirty.append(f"A. Tangencial = {ac}")
	 
		if len(ActEntry.get()) != 0:
			ac = float(ActEntry.get())
			if len(wEntry) == 0 and len(rEntry.get()) != 0:
				r = float(rEntry.get())
				w = calcuAc.w(r, ac)
				values.extend([r, w])
				box_dirty.append(f"V. Angular = {w} m/s")
			if len(rEntry.get()) == 0:
				if len(vTanEntry.get()) != 0:
					vt = float(vTanEntry.get())
					r = calcuAc.r1(vt, ac)
					values.extend([vt, r])
					box_dirty.append(f"Radio = {r} m")

				elif len(wEntry.get()) != 0:
					w = float(wEntry.get())
					r = calcuAc.r2(ac, w)
					values.extend(w, r)
					box_dirty.append(f"Radio = {r} m")

				elif len(pEntry.get()) != 0:
					f = float(pEntry.get())
					r = calcuAc.r3(f, ac)
					values.extend(f, r)
					box_dirty.append(f"Radio = {r} m")

				elif len(tEntry.get()) != 0:
					t = float(tEntry.get())
					r = calcuAc.r4(t, ac)
					values.extend(t, r)
					box_dirty.append(f"Radio = {r} m")

		if len(fcenEntry.get()) == 0 and len(massEntry.get()) != 0 and len(ActEntry.get()):
			m = float(massEntry.get())
			ac = float(ActEntry.get())
			fcen = calcuAc.fcen(m, ac)
			values.extend([m, ac, fcen])
			box_dirty.append(f"Fcen = {fcen}")

		if len(massEntry.get()) == 0 and len(ActEntry.get()) != 0 and len(fcenEntry.get()) != 0:
			ac = float(ActEntry.get())
			fcen = float(fcenEntry.get())
			m = calcuAc.m(ac, fcen)
			values.extend([ac, fcen, m])
			box_dirty.append(f"Mass = {m} kg")

		if len(ActEntry.get()) == 0 and len(massEntry.get()) != 0 and len(fcenEntry.get()) != 0:
			m = float(massEntry.get())
			fcen = float(fcenEntry.get())
			ac = calcuAc.ac5(m, fcen)
			values.extend([m, fcen, ac])
			box_dirty.append(f"A. Tangencial = {ac}")

		not_repeated_values = [e for e in values if e not in not_repeated_values]
		box = [i for i in box_dirty if i not in box]
		msg = ""
		if len(box)!= 0:
			for i in box:
				msg += str(i) + "\n"
		pyperclip.copy(msg)
		print(msg)
		messagebox.showinfo(title="RESULTS", message=msg)

	except ValueError:
		messagebox.showerror(title="ERROR", message="INPUT(s) NOT VALID, PERHAPS YOU MISSED A BOX")



wLabel = Label(text="V. Angular: ")
wLabel.grid(column=0, row=1)

vTan = Label(text="V. Tangencial: ")
vTan.grid(column=0, row=2)

Act = Label(text="Ac. Tangencial")
Act.grid(column=0, row=3)

fcenLabel = Label(text="F. Centripeta: ")
fcenLabel.grid(column=0, row=4)

pLabel = Label(text="Frecuencia: ")
pLabel.grid(column=0, row=5)

tLabel = Label(text="Tiempo (s): ")
tLabel.grid(column=0, row=6)

rLabel = Label(text="Radio (m): ")
rLabel.grid(column=0, row=7)

massLabel = Label(text="Mass (kg): ")
massLabel.grid(column=0, row=8)

wEntry = Entry(width=25, borderwidth=2)
wEntry.grid(column=1, row=1)
wEntry.focus()

vTanEntry = Entry(width=25, borderwidth=2)
vTanEntry.grid(column=1, row=2)

ActEntry = Entry(width=25, borderwidth=2)
ActEntry.grid(column=1, row=3)

fcenEntry = Entry(width=25, borderwidth=2)
fcenEntry.grid(column=1, row=4)

pEntry = Entry(width=25, borderwidth=2)
pEntry.grid(column=1, row=5)

tEntry = Entry(width=25, borderwidth=2)
tEntry.grid(column=1, row=6)

rEntry = Entry(width=25, borderwidth=2)
rEntry.grid(column=1, row=7)

massEntry = Entry(width=25, borderwidth=2)
massEntry.grid(column=1, row=8)

calculate_button = Button(text="Calculate", width=30, borderwidth=3, command=calculate)
calculate_button.grid(column=0, row=9, columnspan=2)

clear_button = Button(text="Clear", width=30, borderwidth=3)
clear_button.grid(column=0, row=10, columnspan=2)

window.mainloop()