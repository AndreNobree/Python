import tkinter as tk
from tkinter import ttk

def mostrar_valores():
    print (w1.get(), w2.get())

janela = tk.Tk()
w1 = ttk.Scale(janela, from_=0, to=50)
w1.pack()
w2 = ttk.Scale(janela, from_=0, to=100, orient=tk.HORIZONTAL)
w2.pack()
ttk.Button(janela, text='Mostrar a Escala', command = mostrar_valores).pack()
janela.mainloop()
