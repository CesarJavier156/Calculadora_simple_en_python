import tkinter as Tk #alias tk
#aqui s definen las ecuaciones
def suma():
    num1=int(entry_num1.get()) #entry num 1 es una caja de texto 1
    num2=int(entry_num2.get()) #entry num 2 es una segunda caja de texto
    resutado=num1+num2
    label_resultado.config(text="Resultado: " + str(resutado))#asigna el valor a una etiqueta

def resta():
    num1=int(entry_num1.get()) #entry num 1 es una caja de texto 1
    num2=int(entry_num2.get()) #entry num 2 es una segunda caja de texto
    resutado=num1-num2
    label_resultado.config(text="Resultado: " + str(resutado))#asigna el valor a una etiqueta    

def multi():
    num1=int(entry_num1.get()) #entry num 1 es una caja de texto 1
    num2=int(entry_num2.get()) #entry num 2 es una segunda caja de texto
    resutado=num1*num2
    label_resultado.config(text="Resultado: " + str(resutado))#asigna el valor a una etiqueta

def divi():
    num1=int(entry_num1.get()) #entry num 1 es una caja de texto 1
    num2=int(entry_num2.get()) #entry num 2 es una segunda caja de texto
    resutado=num1/num2
    label_resultado.config(text="Resultado: " + str(resutado))#asigna el valor a una etiqueta

app=Tk.Tk() #ventana o formulario= app el alias Tk
app.title("TECNOLOGICO DE ESTUDIOS SUPERIORES DE JILOTEPEC" )

label_num1=Tk.Label(text="Primer numero: ")
entry_num1=Tk.Entry()

label_num2=Tk.Label(text="Segundo numero: ")
entry_num2=Tk.Entry()

label_resultado = Tk.Label(text=" **** ")
button_suma=Tk.Button(text="sumar", command=suma)
button_resta=Tk.Button(text="restar", command=resta)
button_muti=Tk.Button(text="multiplicar", command=multi)
button_divi=Tk.Button(text="dividir", command=divi)
    
label_num1.pack()
entry_num1.pack()

label_num2.pack()
entry_num2.pack()

label_resultado.pack()
button_suma.pack()
button_resta.pack()
button_muti.pack()
button_divi.pack()

app.geometry("500x500")
app.mainloop()
