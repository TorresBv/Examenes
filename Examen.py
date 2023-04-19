from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql

class Cliente:
    def __init__(self, root):
        self.wind = root
        self.wind.title("Cliente")
        self.wind.geometry("850x550")
        self.wind.config(bg="teal")

        frame1 = LabelFrame(self.wind, text="Datos del Cliente", font=("calibri", 14))
        frame2 = LabelFrame(self.wind, text="Informacion del Cliente", font=("calibri", 14))
        
        frame1.pack(fill="both", expand="yes", padx=20, pady=15)
        frame2.pack(fill="both", expand="yes", padx=20, pady=15)
        
        ID = StringVar()
        Nombre = StringVar()
        Apellido = StringVar()
        Direccion = StringVar()

        def Agregar():
            if ID.get() =="" or Nombre.get()=="" or Apellido.get()=="" or Direccion.get()=="" :
                messagebox.showerror("Por favor", "Ingrese La Informacion Correcta")
            else:
                base = pymysql.connect(host="localhost", user="root", password="", database="base")
                cursor = base.cursor()
                cursor.execute("insert into cliente values(%s,%s,%s,%s)", (
                
                ID.get(),
                Nombre.get(),
                Apellido.get(),
                Direccion.get(),
                ))
                base.commit
                base.close
                messagebox.showinfo("Datos completado", "Se agregaron Correctamente")


        def Limpiar()
            self.entID.delete(0, END)
            self.entNombre.delete(0, END)
            self.entApellido.delete(0, END)
            self.entDireccion.delete(0, END)


        lbl1 = Label(frame1, text="ID Del Cliente", width=20)
        lbl1.grid(row=0, column=0, padx=5, pady=3)
        self.entID = Entry(frame1, textvariable=ID)
        self.entID.grid(row=0, column=0, padx=5, pady=3)

        lbl2 = Label(frame1, text="Nombre Del Cliente", width=20)
        lbl2.grid(row=1, column=0, padx=5, pady=3)
        self.entNombre = Entry(frame1, textvariable=ID)
        self.entNombre.grid(row=1, column=1, padx=5, pady=3)

        lbl3 = Label(frame1, text="Apellido Del Cliente", width=20)
        lbl3.grid(row=2, column=0, padx=5, pady=3)
        self.entApellido = Entry(frame1, textvariable=ID)
        self.entApellido.grid(row=2, column=1, padx=5, pady=3)

        lbl4 = Label(frame1, text="Direccion Del Cliente", width=20)
        lbl4.grid(row=3, column=0, padx=5, pady=3)
        self.entDireccion = Entry(frame1, textvariable=ID)
        self.entDireccion.grid(row=3, column=1, padx=5, pady=3)

        btn1 =  Button(frame1,text="Agregar", width=12, height=2)
        btn1.grid(row=5, column=0, padx=10, pady=10)

        btn2 =  Button(frame1,text="Eliminar", width=12, height=2)
        btn2.grid(row=5, column=1, padx=10, pady=10)

        btn3 =  Button(frame1,text="Actualizar", width=12, height=2)
        btn3.grid(row=5, column=3, padx=10, pady=10)

        btn4 =  Button(frame1,text="Monitor", width=12, height=2)
        btn4.grid(row=5, column=4, padx=10, pady=10)

        btn5 =  Button(frame1,text="Limpiar", width=12, height=2, command=Limpiar)
        btn5.grid(row=5, column=5, padx=10, pady=10)

        self.trv = ttk.Treeview(frame2, columns=(1,2,3,4), show="headings", height="15")
        self.trv.pack()

        self.trv.heading(1, text="ID Cliente")
        self.trv.heading(2, text="Nombre del Cliente")
        self.trv.heading(3, text="Apellido del Cliente")
        self.trv.heading(4, text="Direccion del Cliente")








