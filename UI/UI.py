from tkinter import *
from tkinter import ttk
from tkinter import messagebox

opcion = ["No data"]
def ventanas():
        global opcion

        ventana = Tk()
        ventana.title('Proyecto 1')
        ventana.geometry("1500x800")


        def cerrar():
            exit()

        def ReporteSecuenciaIn():
            #Boxtextt = TextBoxSeg.get("1.0", 'end-1c')
            messagebox.showinfo(title="Error", message="Ingrese un valor")

        notebook = ttk.Notebook(ventana)
        notebook.pack(fill=BOTH, expand=1)

        s = ttk.Style()
        s.configure('TFrame', background='#949393')

        pes1 = ttk.Frame(notebook)

        notebook.add(pes1, text='Generar Reportes')

        # Pestana 4 ------------------------------------------------------------------------------------
        Label(pes1, text="------------------------------------------------------", font=("Popins", 12)).place(x=10, y=50)

        Button(pes1, text="Salir", command=cerrar).place(x=1400, y=0)

        Label(pes1, text="Codigo", font=("Popins", 12)).place(x=300, y=25)

        Label(pes1, text="Consola",  font=("Popins", 12)).place(x=300, y=575)

        CodeTxt = Text(pes1, width=130, height=30)
        CodeTxt.grid(row=1, column=0)
        CodeTxt.place(x=300, y=60)

        ConsoleTxt = Text(pes1, width=130, height=10)
        ConsoleTxt.grid(row=1, column=0)
        ConsoleTxt.place(x=300, y=600)

        Button(pes1, text="💎RUN💎", command=ReporteSecuenciaIn).place(x=10, y=80)

        # Terminar ------------------------------------------------------------------------------------

        ventana.mainloop()



if __name__ == "__main__":

    ventanas()
