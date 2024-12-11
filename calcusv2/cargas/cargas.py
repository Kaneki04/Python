from tkinter import *
from tkinter import messagebox
from cargascalcu import Cargas
import pyperclip

calcuCarga = Cargas("Cargas")
window = Tk()
window.config(padx=10, pady= 10)
window.title(calcuCarga.name)


def calculate():
    gets = [q1Entry.get(), q2Entry.get(), dEntry.get(), fEntry.get()]
    variable = [gets.index(i) for i in gets if len(i) == 0]
    try:
        if 0 in variable:
            q1 = calcuCarga.q1(float(q2Entry.get()), float(dEntry.get()), float(fEntry.get()))
            pyperclip.copy(q1)
            messagebox.showinfo(title="Result", message=f"Q1 = {q1} C/N")
            gets.clear()
            variable.clear()
        elif 1 in variable:
            q2 = calcuCarga.q2(float(q1Entry.get()), float(dEntry.get()), float(fEntry.get()))
            pyperclip.copy(q2)
            messagebox.showinfo(title="Result", message=f"Q2 = {q2} C/N")
            gets.clear()
            variable.clear()
        elif 2 in variable: 
            d = calcuCarga.d(float(q1Entry.get()), float(q2Entry.get()), float(fEntry.get()))
            pyperclip.copy(d)
            messagebox.showinfo(title="Result", message=f"Distance = {d} m")
            gets.clear()
            variable.clear()
        elif 3 in variable:
            f = calcuCarga.f(float(q1Entry.get()), float(q2Entry.get()), float(dEntry.get()))
            pyperclip.copy(f)
            messagebox.showinfo(title="Result", message=f"Atraction force = {f} N")
            gets.clear()
            variable.clear()
    except ValueError:
        messagebox.showerror("Error", "INPUT(s) NOT VALID, PERHAPS YOU MISSED A BOX")

def clear():
    q1Entry.delete(0, END)
    q2Entry.delete(0, END)
    dEntry.delete(0, END)
    fEntry.delete(0, END)
    q1Entry.focus()



logo = PhotoImage(file="Atomic-Electron-Cloud-Illustration (1).png")
canvas = Canvas(height=160, width=250)
canvas.create_image(130, 80, image=logo)
canvas.grid(column=0, row=0, columnspan=2)

q1label = Label(text="Insert value for Q1 (mC):  ")
q1label.grid(column=0, row=1)

q2label = Label(text="Insert value for Q2 (mC):  ")
q2label.grid(column=0, row=2)

dlabel = Label(text="Insert value for Distance (m): ")
dlabel.grid(column=0, row=3)

flabel = Label(text="Insert value for Force (N/C): ")
flabel.grid(column=0, row=4)

q1Entry = Entry(width=25, borderwidth=2)
q1Entry.focus()
q1Entry.grid(column=1, row=1, pady=2)

q2Entry = Entry(width=25, borderwidth=2)
q2Entry.grid(column=1, row=2, pady=2)

dEntry = Entry(width=25, borderwidth=2)
dEntry.grid(column=1, row=3, pady=2)

fEntry = Entry(width=25, borderwidth=2)
fEntry.grid(column=1, row=4, pady=2)

calcButton = Button(text="Calculate", width=30, command=calculate, borderwidth=3)
calcButton.grid(column=0, row=5, columnspan=2, pady=2)

clear_button = Button(text="Clear", width=30, command=clear, borderwidth=3)
clear_button.grid(column=0, row=6, columnspan=2, pady=2)

window.mainloop()