import tkinter as tk
from tkinter import ttk, messagebox
import re

app = tk.Tk()
app.title("Actividad 2 Ramirez Mendez Diego Ernesto")
app.geometry("500x350")
app.resizable(False,False)

expresiones = {
    "Teléfono de 10 digitos": r"^\d{10}$", #
    "Correo electrónico": r"^[\w\.-]+@[\w\.-]+\.\w+$", #
    "CURP": r"^[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z0-9]\d$", #
    "Contraseña segura": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$", #
    "Direccion IP v4": r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$", #
    "Direccion IP v6": r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$", #
    "RFC": r"^[A-ZÑ&]{3,4}\d{6}[A-Z0-9]{3}$", #
    "Cumpleaños": r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$", #
    "Placas de automovil": r"^[A-Z]{3}-\d{3}$", #
}



label_texto = tk.Label(app, text="Ingrese el texto que quiere validar:")
label_texto.pack(pady=5)

entrada_texto = tk.Entry(app, width=40)
entrada_texto.pack(pady=5)

label_opcion = tk.Label(app, text="Seleccione la expresion:")
label_opcion.pack(pady=5)

opcion = tk.StringVar()
combo = ttk.Combobox(app, textvariable=opcion, state="reandoly", width=35)
combo["values"] = list(expresiones.keys())
combo.pack(pady=5)
combo.current(0)

def validar():
    texto = entrada_texto.get()
    seleccion = opcion.get()

    patron = expresiones[seleccion]

    if re.fullmatch(patron, texto):
        messagebox.showinfo("Resultado", "El texto SI es valido.")
    else:
        messagebox.showinfo("Resultado", "El texto NO es valido.")

boton_validar = tk.Button(app, text="Validar", command=validar)
boton_validar.pack(pady=20)

app.mainloop()