# Utilizando widgets temáticos
# Utilizando argumentos de palavra chave. # Similar ao que ocorre nos temas dos cartões no git hub

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

# Usando argumentos de palavra-chave ao criar o widget
ttk.Label(root,text='Ola mundo1!').pack() # Texto dentro da aplicação


# Usando um índice de dicionário após a criação do widget
lbl1 = ttk.Label(root) # Definindo que o label é referente a root, pagina principal
lbl1['text'] = 'Outro Olá mundo!' # Definindo ao atributo que ele pertence
lbl1.pack()

# Usando o metodo config() com atributos de palavra-chave
lbl2 = ttk.Label(root) # Referenciado novamente a pagina principal
lbl2.config(text ='Terceiro Olá mundo!') # Adicionando mais um valor ao Label
lbl2.pack()



root.mainloop()