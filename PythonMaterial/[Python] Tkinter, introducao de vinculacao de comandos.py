# Introdução de vinculação de comandos do Tkinter
# O básico do processo de ação da aplicação gerada, atribuindo a um comando uma função que contem uma determinada ação

import tkinter as tk

# Modelo de aplicação do import do módulo classico
from tkinter import ttk 

root= tk.Tk()
root.title('Introdução aos Widgets temáticos TTK')


# Criando função de comando para realizar uma determinada ação ao utilizar um botão
def button_clicked():
    root.config(background='#00ffff') # Altera as cores na aplicação para o código hexadecimal informado
    print('O comando funcionou!') # Exibe a mensagem no terminal

 # Criando botão
btn = ttk.Button(root,text='Pressione.', command=button_clicked) # Desta forma a função está vinculada ao evento de clique do botão
btn.pack() # Exibe o botão na tela
   

# Config de Tela
root.resizable(1,1)
root.state('normal')

screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()

wind_x = 600
wind_y = 400

center_x = int(screen_x/2 - wind_x/2)
center_y = int(screen_y/2 - wind_y/2)

root.geometry(f'{wind_x}x{wind_y}+{center_x}+{center_y}')






root.iconbitmap('C:\\Users\\Raul\\Downloads\\Icone.ico')


root.mainloop()