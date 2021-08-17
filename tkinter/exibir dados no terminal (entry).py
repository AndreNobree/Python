# Widget Entry
import tkinter as tk

def mostrar_nomes():
    print('Nome: %s\nSobrenome: %s' % (nome.get(), sobrenome.get()))

janela = tk.Tk()
janela.title('Aplicação GUI como Widget Entry')
#posicionar o nome antes da tabela (nome: \_________| )
tk.Label(janela, text = 'Nome: ').grid(row = 0) 
tk.Label(janela, text = 'Sobrenome: ').grid(row = 1)
#vai mostrar que é do tipo entry(inserir dados)
nome = tk.Entry(janela)
sobrenome = tk.Entry(janela)
# posicionar na janela
nome.grid(row = 0, column = 1)
sobrenome.grid(row = 1, column = 1)
tk.Button(janela, text = 'Sair', fg = 'white', bg = 'red', command = janela.quit).grid(row = 3, column = 0, sticky = tk.W, pady = 4)
tk.Button(janela, text = 'Exibir Dados', fg = 'white', bg = 'blue',command = mostrar_nomes).grid(row = 3, column = 1, sticky = tk.W, pady = 4)
tk.mainloop()
