# Introdução a interação das teclas do teclado com os comandos da aplicação
# Foi demonstrado o limite de interações entre as teclas do teclado e a aplicação.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Limitações de ligaçao de comando')
# Dimensões da janela da aplicação
wind_x = 600
wind_y = 400
# Dimensões da tela
screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()
# Config de centro de tela
center_x = int(screen_x/2 - wind_x/2)
center_y = int(screen_y/2 - wind_y/2)

root.geometry(f'{wind_x}x{wind_y}+{center_x}+{center_y}')
#----

def select(arg):
    root.config(background=arg)

btn1=ttk.Button(root,text= 'Digite a cor no terminal', command=lambda:select(input('Digite a cor:')))
btn1.pack()

root.mainloop()