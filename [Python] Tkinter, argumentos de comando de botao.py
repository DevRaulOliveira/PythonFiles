# Argumentos de comando do botão Tkinter
# Aprendizado de argumentos em botões
# Aprendizado de caixa de confirmação

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Argumentos de botões')

# Configurações de tela
wind_w = 600
wind_h = 400

screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()

center_x = int(screen_x/2-wind_w/2)
center_y = int(screen_y/2 - wind_h/2)

root.geometry(f'{wind_w}x{wind_h}+{center_x}+{center_y}')

root.iconbitmap('C:\\Users\\rol5oy\\Pictures\\Fb.ico')

def select(arg): # Permite que seja inseridos informações como argumentos
    root.config(background=arg)

# Construtor do botão
btn = ttk.Button(root,text ='Pressione para mudar a cor, no terminal:', # text = Mensagem expressa no botão
                 command= lambda:select(input('Digite o nome da cor:')))   # Command=lambda: permite a execução dos argumentos da função, neste caso ao pressionar o botão, aparece a mensagem no terminal para informar a cor tanto em formato de string, quanto em hexadecimal
btn.pack() # Permite a exibição do botão na aplicação


# Costrutor de caixa de confirmação
check = ttk.Checkbutton(root,text='Modelo de caixa de check') # Modelo de criação da caixa de texto
check.pack()

# Contrutor de caixa de texto
textbox = ttk.Entry(root,text ='Modelo de caixa de texto')
textbox.pack()

root.mainloop()