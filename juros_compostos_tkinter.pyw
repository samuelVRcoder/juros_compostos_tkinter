import tkinter as tk
from tkinter import messagebox as msg

frame = tk.Tk() 
frame.title("Juros Calc") 
frame.geometry('200x200')
frame.resizable(False, False)
  
def calc():
    try:
        c = inputcap.get(1.0, "end-1c")
        i = inputtax.get(1.0, "end-1c")
        t = inputtime.get(1.0, "end-1c")
        
        
        c = float(str(c).replace(",", "."))
        i = float(str(i).replace(",", "."))
        t = float(str(t).replace(",", "."))
        formula = c*((1+(i/100))**t)

        formula_str = f"{formula:.2f}"

        msg.showinfo("Resultado", formula_str)
    except Exception as e:
        msg.showinfo("Erro", "Algo deu errado\n\n"+str(e))

lblnome = tk.Label(frame, text = "Capital Inicial") 
lblnome.pack()  
 
inputcap = tk.Text(frame, 
                   height = 1, 
                   width = 20)
inputcap.pack()

lblfone = tk.Label(frame, text = "Taxa") 
lblfone.pack()


inputtax = tk.Text(frame, 
                   height = 1, 
                   width = 20)
  
inputtax.pack()

lblfone = tk.Label(frame, text = "Tempo em anos") 
lblfone.pack()


inputtime = tk.Text(frame, 
                   height = 1, 
                   width = 20)
  
inputtime.pack() 
  
 
printButton = tk.Button(frame, 
                        text = "Calcular Montante",  
                        command = calc) 
printButton.pack()

frame.mainloop()
