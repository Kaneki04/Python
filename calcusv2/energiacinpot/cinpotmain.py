from tkinter import *
from tkinter import messagebox
from cinpotcalcu import Energy
import pyperclip

calcu = Energy("Energy Calculator")
window = Tk()
window.config(padx=10, pady=10)
window.title(calcu.name)

canvas = Canvas()
logo = PhotoImage(file=calcu.logo)
canvas.create_image(192, 125, image=logo)
canvas.grid(column=0, row=0, columnspan=2, pady=5)

def calculate():
    m = float
    h = float
    v = float
    ec = float
    ep = float
    g = float
    calculations_in_box = []
    possible_answers = []
    try:
        if len(mEntry.get()) == 0 and len(epEntry.get()) != 0 and len(gEntry.get()) != 0 and len(hEntry.get()) != 0:
            m = calcu.massv1(float(epEntry.get()), float(gEntry.get()), float(hEntry.get()))
            ep = float(epEntry.get())
            g = float(gEntry.get())
            h = float(hEntry.get())
            possible_answers.extend([m, ep, g, h])
            calculations_in_box.append(f"Mass = {m} kg")

        elif len(mEntry.get()) == 0 and len(ecEntry.get()) != 0 and len(vEntry.get()) != 0:   
            m = calcu.massv2(float(ecEntry.get()), float(vEntry.get()))
            ec = float(ecEntry.get())
            v = float(vEntry.get())
            possible_answers.extend([m, ec, v])
            calculations_in_box.append(f"Mass = {m} kg")

        if len(hEntry.get()) == 0 and len(epEntry.get()) != 0 and len(gEntry.get()) != 0 and len(mEntry.get()) != 0:
            h = calcu.height(float(epEntry.get()), float(gEntry.get()), float(mEntry.get()))
            m = float(mEntry.get())
            ep = float(epEntry.get())
            g = float(gEntry.get())
            possible_answers.extend([h, m, ep, g])
            calculations_in_box.append(f"Height = {h} m") 

        if len(vEntry.get()) == 0 and len(ecEntry.get()) != 0 and len(mEntry.get()):
            v = calcu.velocity(float(ecEntry.get()), float(mEntry.get()))
            ec = float(ecEntry.get())
            m = float(mEntry.get())
            possible_answers.extend([v, ec, m]) 
            calculations_in_box.append(f"Velocity = {v} m/s")

        if len(ecEntry.get()) == 0 and len(mEntry.get()) != 0 and len(vEntry.get()) != 0:
            ec = calcu.ecin(float(mEntry.get()), float(vEntry.get()))
            m = float(mEntry.get())
            v = float(vEntry.get())
            possible_answers.extend([ec, m, v])
            calculations_in_box.append(f"Kinetic Energy = {ec} J")

        if len(epEntry.get()) == 0 and len(mEntry.get()) != 0 and len(hEntry.get()) != 0 and len(gEntry.get()) != 0:
            ep = calcu.epot(float(mEntry.get()), float(hEntry.get()), float(gEntry.get()))
            m = float(mEntry.get())
            h = float(hEntry.get())
            g = float(gEntry.get())
            possible_answers.extend([ep, m, h, g])
            calculations_in_box.append(f"Potential Energy = {ep} J")

        if len(gEntry.get()) == 0 and len(epEntry.get()) != 0 and len(hEntry.get()) != 0 and len(mEntry.get()) != 0:
            g = calcu.gravity(float(epEntry.get()), float(hEntry.get()), float(mEntry.get()))
            m = float(mEntry.get())
            h = float(hEntry.get())
            ep = float(epEntry.get())
            possible_answers.extend([g, m, h, ep])
            calculations_in_box.append(f"Gravity = {g} m/s^2")

        if v not in possible_answers and ec in possible_answers and m in possible_answers:
            v = calcu.velocity(ec, m)
            calculations_in_box.append(f"Velocity = {v} m/s")

        if len(calculations_in_box) != 0:
            box = ""
            for i in calculations_in_box:
                box += str(i) + "\n"
            pyperclip.copy(box)
            messagebox.showinfo(title="RESULTS", message=box)

        else:
            messagebox.showerror(title="ERROR", message="INPUT(s) NOT VALID, PERHAPS YOU MISSED A BOX")

    except ValueError:
        messagebox.showerror(title="ERROR", message="INPUT(s) NOT VALID, PERHAPS YOU MISSED A BOX")
def clear():
    mEntry.delete(0, END)
    hEntry.delete(0, END)
    epEntry.delete(0, END)
    gEntry.delete(0, END)
    ecEntry.delete(0, END)
    vEntry.delete(0, END)
    mEntry.focus()

def ok_function(event):
    calculate()

# Labels
mLabel = Label(text="Insert mass (kg): ")
mLabel.grid(column=0, row=1)

hLabel = Label(text="Insert height (m): ")
hLabel.grid(column=0, row=2)

gLabel = Label(text="Insert gravity (m/s^2): ")
gLabel.grid(column=0, row=3)

ecLabel = Label(text="Insert Kinetic Energy (J): ")
ecLabel.grid(column=0, row=4)

epLabel = Label(text="Insert Potential Energy (J): ")
epLabel.grid(column=0, row=5)

vLabel = Label(text="Insert velocity (m/s): ")
vLabel.grid(column=0, row=6)


# Entries
mEntry = Entry(width=30, borderwidth=2)
mEntry.focus()
mEntry.grid(column= 1, row=1, sticky="w", pady=2)

hEntry = Entry(width=30, borderwidth=2)
hEntry.grid(column=1, row=2, sticky="w", pady=2)

gEntry = Entry(width=30, borderwidth=2)
gEntry.grid(column=1, row=3, sticky="w", pady=2)

ecEntry = Entry(width=30, borderwidth=2)
ecEntry.grid(column=1, row=4, sticky="w", pady=2)

epEntry = Entry(width=30, borderwidth=2)
epEntry.grid(column=1, row=5, sticky="w", pady=2)

vEntry = Entry(width=30, borderwidth=2)
vEntry.grid(column=1, row=6, sticky="w", pady=2)

# Buttons
calcButton = Button(text="Calculate", width=30, borderwidth=4, command=calculate)
calcButton.grid(column=0, row=7, columnspan=2)

clearButton = Button(text="Clear", width=30, borderwidth=4, command=clear)
clearButton.grid(column=0, row=8, columnspan=2, pady=3)

window.bind("<Return>", ok_function)

window.mainloop()