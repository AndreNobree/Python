# Widget Message
import tkinter as tk
janela = tk.Tk()
mensagem_para_usuario = 'Olá Usuário'
msg = tk.Message(janela, text = mensagem_para_usuario)
msg.config(bg = 'lightblue', font = ('verdana', 20, 'italic'))
msg.pack()
janela.mainloop()
