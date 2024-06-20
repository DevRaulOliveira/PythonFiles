# Associação de evento no Tkinter
# Metodo Band, contém o detalhe do evento, sendo possível ter vários manipuladores de evento ligado ao mesmo evento
# <return> é o nome da tecla enter para ser utilizada para interagir com a aplicação
# Todo botão precisa de um comand para executar alguma ação


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
# Adicionando um evento a uma função

def return_pressed(event):
    print('Tecla enter pressionada.')
btn = ttk.Button(root,text = 'Executar')
# Utilizando o metodo BIND o mesmo usado em jogos para atribuir comandos a uma tecla do teclado
btn.bind('<Return>',return_pressed) # Evento de tecla enter pressionada. Desta forma a tecla ao ser pressionada executa a função
btn.focus() # Atribui esse foco extra de interação ao pressionar a tecla # O botão já começa com esse foco
btn.pack(expand=True)

root.mainloop()