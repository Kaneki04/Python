vi = input("Velocidad Inicial m/s: ")
vf = input("Velocidad Final m/s: ")
t = input("Tiempo s: ")
a = input("Aceleracion m/s**2: ")
xi = input("Posicion Inicial m: ")

if vi != "":
    vi = float(vi)
if vf != "":
    vf = float(vf)
if t != "":
    t = float(t)
if a != "":
    a = float(a)
if xi != "":
    xi = float(xi)

if xi != "" and vi != "" and t != "":
    xf = xi + (vi*t) + ((1/2)*a*(t**2))
    print(f"xF = {xf}")

if a == "" and vi != "" and vf != "" and t != "":
    a = (vf - vi) / t
    print(f"Aceleracion = {a}")

if t == "" and vi != "" and vf != "" and a != "":
    t = (vi - vf)/a
    print(f"Tiempo = {t}")

if vf == "" and vi != "" and a != "" and t != "":
    vf = vi + (a*t)
    print(f"Vf = {vf}")
