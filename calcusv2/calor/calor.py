from tkinter import *
from tkinter import messagebox
from caloroop import Calor
import pyperclip

calcuCalor = Calor("Heat")
window = Tk()
window.config(padx=10, pady= 10)
window.title(calcuCalor.name)

logo = PhotoImage(file="sun.png")
canvas = Canvas(height=300, width=300)
canvas.create_image(150, 150, image=logo)
canvas.grid(column=0, row=0, columnspan=2)

def calculate():
    try:
        gets = [m1Entry.get(), ce1Entry.get(), ti1Entry.get(), m2Entry.get(), ce2Entry.get(), ti2Entry.get(), tfEntry.get()]
        variable = [gets.index(i) for i in gets if len(i) == 0]
        if 0 in variable:
            m1 = calcuCalor.m1(float(ti1Entry.get()), float(ce1Entry.get()), float(m2Entry.get()), float(ce2Entry.get()), float(ti2Entry.get()), float(tfEntry.get()))
            pyperclip.copy(f"{m1} kg")
            messagebox.showinfo(title="Result", message=f"M1 = {m1} kg")
            gets.clear()
            variable.clear()
        elif 1 in variable:
            ce1 = calcuCalor.ce1(float(m1Entry.get()), float(ti1Entry.get()), float(m2Entry.get()), float(ce2Entry.get()), float(ti2Entry.get()), float(tfEntry.get()))
            pyperclip.copy(f"{ce1} J/(kg*K)")
            messagebox.showinfo(title="Result", message=f"Ce1 = {ce1} J/(kg*K)")
            gets.clear()
            variable.clear()
        elif 2 in variable:
            ti1 = calcuCalor.ti1(float(m1Entry.get()), float(ce1Entry.get()), float(m2Entry.get()), float(ti2Entry.get()), float(ce2Entry.get()), float(tfEntry.get()))
            pyperclip.copy(f"{ti1} K")
            messagebox.showinfo(title="Result", message=f"Ti1 = {ti1} K")
            gets.clear()
            variable.clear()
        elif 3 in variable:
            m2 = calcuCalor.m2(float(m1Entry.get()), float(ti1Entry.get()), float(ce1Entry.get()), float(ce2Entry.get()), float(ti2Entry.get()), float(tfEntry.get()))
            pyperclip.copy(f"{m2} kg")
            messagebox.showinfo(title="Result", message=f"M2 = {m2} kg")
            gets.clear()
            variable.clear()
        elif 4 in variable:
            ce2 = calcuCalor.ce2(float(m1Entry.get()), float(ce1Entry.get()), float(ti1Entry.get()), float(m2Entry.get()), float(ti2Entry.get()), float(tfEntry.get()))
            pyperclip.copy(f"{ce2} J/(kg*K)")
            messagebox.showinfo(title="Result", message=f"Ce2 = {ce2} J/(kg*K)")
            gets.clear()
            variable.clear()
        elif 5 in variable:
            ti2 = calcuCalor.ti2(float(m1Entry.get()), float(ce1Entry.get()), float(ti1Entry.get()), float(m2Entry.get()), float(ce2Entry.get()), float(tfEntry.get()))
            pyperclip.copy(f"{ti2} k")
            messagebox.showinfo(title="Result", message=f"Ti2 = {ti2} k")
            gets.clear()
            variable.clear()
        elif 6 in variable:
            tf = calcuCalor.tf(float(m1Entry.get()), float(ce1Entry.get()), float(ti1Entry.get()), float(m2Entry.get()), float(ce2Entry.get()), float(ti2Entry.get()))
            pyperclip.copy(f"{tf} K")
            messagebox.showinfo(title="Result", message=f"Tf = {tf} k")
            gets.clear()
            variable.clear()
    except ValueError:
        messagebox.showerror(title="ERROR", message=f'"{ValueError}"\nEnter a Valid Number\n(Check if any White Spaces)')

def clearf():
    m1Entry.delete(0, END)
    ce1Entry.delete(0, END)
    ti1Entry.delete(0, END)
    m2Entry.delete(0, END)
    ce2Entry.delete(0, END)
    ti2Entry.delete(0, END)
    tfEntry.delete(0, END)
    m1Entry.focus()

def calculatebind(event):
    calculate()

def clearf_button(event):
    clearf()

m1label = Label(text="Mass 1 (kg):")
m1label.grid(column=0, row=1)

ce1label = Label(text="Specific Heat 1 (J/(kg*K)): ")
ce1label.grid(column=0, row=2)

ti1label = Label(text="Initial Temperature 1 (°C):")
ti1label.grid(column=0, row=3)

m2label = Label(text="Mass 2 (kg):")
m2label.grid(column=0, row=4)

ce2label = Label(text="Specific Heat 2 (J/(kg*K)):")
ce2label.grid(column=0, row=5)

ti2label =Label(text="Initial Temperature 2 (°C):")
ti2label.grid(column=0, row=6)

tfLabel = Label(text="Final Temperature (C):")
tfLabel.grid(column=0, row=7)

m1Entry = Entry(width=25, borderwidth=2)
m1Entry.grid(column=1, row=1, pady=2)
m1Entry.focus()

ce1Entry = Entry(width=25, borderwidth=2)
ce1Entry.grid(column=1, row=2, pady=2)

ti1Entry = Entry(width=25, borderwidth=2)
ti1Entry.grid(column=1, row=3, pady=2)

m2Entry = Entry(width=25, borderwidth=2)
m2Entry.grid(column=1, row=4, pady=2)

ce2Entry = Entry(width=25, borderwidth=2)
ce2Entry.grid(column=1, row=5, pady=2)

ti2Entry = Entry(width=25, borderwidth=2)
ti2Entry.grid(column=1, row=6, pady=2)

tfEntry = Entry(width=25, borderwidth=2)
tfEntry.grid(column=1, row=7, pady=2)

calculate_button = Button(text="Calculate", width=30, borderwidth=3, command=calculate)
calculate_button.grid(column=0, row=8, columnspan=2)

clear_button = Button(text="Clear", width=30, borderwidth=3, command=clearf)
clear_button.grid(column=0, row=9, columnspan=2)
window.bind("<Return>", calculatebind)
window.bind("<Control-Shift-C>", clearf_button)
window.mainloop()