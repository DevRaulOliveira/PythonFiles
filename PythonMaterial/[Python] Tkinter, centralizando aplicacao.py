# Centralizando uma aplicação em Python

import tkinter as tk

root = tk.Tk()
root.title('Aplicação centralizada')

window_width = 300
window_height = 200

# Obtendo as dimensões da tela
screen_width = root.winfo_screenwidth() # Largura da tela
screen_height = root.winfo_screenheight() # Altura da tela

# Encontrando o ponto central da tela

center_x = int((screen_width/2) -(window_width/2)) # É preciso que o resultado encontrado retorne um valor inteiro
center_y = int((screen_height/2)-(window_height/2))


# Definir a posição da janela no centro da tela
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.mainloop()