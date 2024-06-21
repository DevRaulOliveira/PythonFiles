# Associando mais de um manipulador a um evento no Tkinter
# Comando ADD é o comando utilizado para adicionar mais de uma ação a um evento
# Caso não seja utilizado o ADD a informação anterior será substituida pelo novo evento
# Com a execução desse evento irão ocorrer simultaneamente as duas ações

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Associação de eventos')

wind_x = 600
wind_y = 400
# root.state('zoomed')
# root.resizable(1,1)


screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()

center_x = int((screen_x/2) - (wind_x/2))
center_y = int((screen_y/2) - (wind_y/2))

root.geometry(f'{wind_x}x{wind_y}+{center_x}+{center_y}')
root.iconbitmap('C:\\Users\\Raul\\Downloads\\Icone.ico')

#---

# Adicionando mais de um manipulador a um evento

def return_pressed(event): # Primeiro evento
    print('Tecla enter pressionada.')

def log(event): # Segundo evento
    print(event)

btn = ttk.Button(root,text = 'Executar')
#  Evento 1 - Exibe a mensagem da função no terminal
btn.bind('<Return>',return_pressed) # Primeiro evento. Desta forma a tecla ao ser pressionada executa a função

# Evento 2 - Modelo de uso do comando ADD. Adiciona o caractere '+'
btn.bind('<Return>',log,add="+") # Segundo evento. Exibe o caracte '+'
btn.focus() # Atribui esse foco extra de interação ao pressionar a tecla # O botão já começa com esse foco
btn.pack(expand=True)

root.mainloop()