from tkinter import ttk
from tkinter import *
from tkinter import messagebox   
import pymysql

class regis:
    def __init__(self, root):
        self.wind = root
        self.wind.title("Registro De Ventas")
        self.wind.geometry("850x600")
        self.wind.config(bg="orange")


        frame1 = LabelFrame(self.wind, text="Datos De La Venta", bg="aqua", font=("Arial", 14))
        frame2 = LabelFrame(self.wind, text="Informacion", bg="aqua", font=("Arial", 14))

        frame1.pack(fill="both", expand="yes", padx=20, pady=15)  
        frame2.pack(fill="both", expand="yes", padx=20, pady=15)

        
        ID = StringVar()
        Producto = StringVar()
        Piezas = StringVar()
        Precio = StringVar()
       
        def Agregar():
            if ID.get() =="" or Producto.get()=="" or Piezas.get()=="" :
                messagebox.showerror("Por favor", "Ingrese La Informacion Correcta")
            else:
                unidad2 = pymysql.connect(host="localhost", user="root", password="", database="unidad2")
                cursor = unidad2.cursor()
                cursor.execute("insert into regis values(%s,%s,%s,%s)", (

                ID.get(),
                Producto.get(),
                Piezas.get(),
                Precio.get(),
                ))
                unidad2.commit() 
                unidad2.close() 
                messagebox.showinfo("Datos Completado", "Se agregaron correctamente")  

        def Limpiar():
            self.entID.delete(0, END) 
            self.entProducto.delete(0, END) 
            self.entPiezas.delete(0, END) 
            self.entPrecio.delete(0, END)  

        def Mostrar():
            unidad2 = pymysql.connect(host="localhost", user="root", password="", database="unidad2")
            cursor = unidad2.cursor()
            cursor.execute("select * from regis")
            result = cursor.fetchall()
            if len(result) != 0:
                self.trv.delete(*self.trv.get_children())
                for row in result:
                    self.trv.insert('',END,values =row) 
            unidad2.commit()
            unidad2.close()  

        def traineeInfo(ev):
            viewInfo =   self.trv.focus()
            learnerData =  self.trv.item(viewInfo) 
            row = learnerData['values'] 
            ID.set(row[0])
            Producto.set(row[1])
            Piezas.set(row[2])
            Precio.set(row[3]) 


        def Actualizar():
            unidad2 = pymysql.connect(host="localhost", user="root", password="", database="unidad2")
            cursor = unidad2.cursor()
            cursor.execute("update regis set producto=%s,piezas=%s,precios=%s where idservicios=%s", (
            Producto.get(), 
            Piezas.get(),
            Precio.get(),
            ID.get()
            ))   
            unidad2.commit()
            Mostrar()
            unidad2.close()  

        def Buscar():
            try: 
                unidad2 = pymysql.connect(host="localhost", user="root", password="", database="unidad2")
                cursor = unidad2.cursor()
                cursor.execute("select * from regiss where nombre='%s'"%Producto.get())

                row = cursor.fetchone()

                ID.set(row[0])
                Producto.set(row[1])
                Piezas.set(row[2])
                Precio.set(row[3]) 

                unidad2.commit()  
            except:
                Limpiar()
            unidad2.close() 

        def Eliminar(): 
            unidad2 = pymysql.connect(host="localhost", user="root", password="", database="unidad2")
            cursor = unidad2.cursor()
            cursor.execute("delete from regis where idservicio=%s",ID.get())
            unidad2.commit()
            Mostrar()
            unidad2.close()
            Limpiar()                 
        

        lbl1 = Label(frame1, text="ID Del Producto", bg="pink", width=20)
        lbl1.grid(row=0, column=0, padx=5, pady=3)
        self.entID = Entry(frame1, textvariable=ID)   
        self.entID.grid(row=0, column=1, padx=5, pady=3) 

        lbl2 = Label(frame1, text="Nombre Del Producto", bg="greenyellow", width=20)
        lbl2.grid(row=1, column=0, padx=5, pady=3)
        self.entProducto = Entry(frame1, textvariable=Producto)   
        self.entProducto.grid(row=1, column=1, padx=5, pady=3) 

        lbl3 = Label(frame1, text="Piezas del Producto", bg="mediumpurple", width=20)
        lbl3.grid(row=2, column=0, padx=5, pady=3)
        self.entPiezas = Entry(frame1, textvariable=Piezas)   
        self.entPiezas.grid(row=2, column=1, padx=5, pady=3) 

        lbl4 = Label(frame1, text="Precio Del Producto", bg="gold", width=20)
        lbl4.grid(row=3, column=0, padx=5, pady=3)
        self.entPrecio = Entry(frame1, textvariable=Precio)   
        self.entPrecio.grid(row=3, column=1, padx=5, pady=3)

        btn1 = Button(frame1, text="Agregar", width=12, height=2, command=Agregar)
        btn1.grid(row=6, column=0, padx=10, pady=10)
        btn1.config(bg="yellow")

        btn2 = Button(frame1, text="Eliminar", width=12, height=2, command=Eliminar)
        btn2.grid(row=6, column=1, padx=10, pady=10)
        btn2.config(bg="lawngreen")

        btn3 = Button(frame1, text="Actualizar", width=12, height=2, command=Actualizar)
        btn3.grid(row=6, column=2, padx=10, pady=10)
        btn3.config(bg="coral")

        btn4 = Button(frame1, text="Mostrar", width=12, height=2, command=Mostrar)
        btn4.grid(row=6, column=3, padx=10, pady=10)
        btn4.config(bg="orchid")

        btn5 = Button(frame1, text="Limpiar", width=12, height=2, command=Limpiar)
        btn5.grid(row=6, column=4, padx=10, pady=10)
        btn5.config(bg="pink")

        btn6 = Button(frame1, text="Buscar", width=12, height=2, command=Buscar) 
        btn6.grid(row=6, column=5, padx=10, pady=10)
        btn6.config(bg="aquamarine")

        self.trv = ttk.Treeview(frame2, columns=(1,2,3,4), show="headings", height="15")
        self.trv.pack()

        self.trv.heading(1, text="ID Cliente")
        self.trv.heading(2, text="Nombre Del Producto")
        self.trv.heading(3, text="Numero De Piezas")
        self.trv.heading(4, text="Total Del Producto")
        self.trv.bind("<ButtonRelease-1>",traineeInfo)



if __name__ == '__main__':
    root = Tk()
    regis = regis(root)
    root.mainloop()