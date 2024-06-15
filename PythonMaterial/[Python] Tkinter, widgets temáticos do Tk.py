# Introdução aos widgets temáticos do Tkinter
# O Tkinter possui duas gerações de temas
# Tem widgets de 1991 e os temáticos são de 2007
# A importação de Widgets temáticos vem do submodulo TTK

import tkinter as tk

# Modelo de aplicação do import do módulo classico
from tkinter import ttk 

root= tk.Tk()
root.title('Introdução aos Widgets temáticos TTK')


# Config de Tela
root.resizable(1,1)
root.state('zoomed')

screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()

wind_x = 600
wind_y = 400

center_x = int(screen_x/2 - wind_x/2)
center_y = int(screen_y/2 - wind_y/2)

root.geometry(f'{wind_x}x{wind_y}+{center_x}+{center_y}')

root.iconbitmap('C:\\Users\\Raul\\Downloads\\Icone.ico')

# Modelo de implementação da modificação do tema da aplicação
tk.Label(root,text='Label Classico').pack()
ttk.Label(root,text='Label Temático').pack() # Fica dessa forma

# Modelo de criação de botões
tk.Button(root,text='Botão classico').pack() # Button é utilizado para criar botões na aplicação
ttk.Button(root,text='Botão temático').pack()

root.mainloop()