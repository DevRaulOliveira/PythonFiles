# Ordem de empilhamento da janela
# A ordenação de janelas segue o conceito de pilha
# '-topmost' garante que a janela da aplicação sempre esteja no topo
# Metodo LIFT = faz com que a janela seja posicionada acima
# Metodo LOWER = faz com que a janela seja posicionada abaixo

import tkinter as tk

root = tk.Tk()

root.title('Ordem de empilhamento de janela')

def main_win_config(): # Agrupando tudo em uma unica função, quando chamada, executa as configurações de tela criadas
    root.state('zoomed')
    root.resizable(1,1)
    # Dimensões da janela
    window_width  = 600
    window_height = 400

    # Dimensões da tela
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()

    # Centralizando a tela, SEMPRE CONVERTER O VALOR PARA UM NUMERO INTEIRO.
    center_y = int(screen_height/2 - window_height/2)
    center_x = int(screen_width/2 - window_width/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    # ORDENANDO JANELAS DA APLICAÇÃO
    root.attributes('-topmost',1) # Coloca a janela no topo de todas as outras aplicações
    # Metodo Lift
    root.lift() # Move a janela para cima na sequencia de janelas da aplicação
    # Metodo lower
    root.lower() # Move a janela para baixo na sequencia de janelas da aplicação

    #



win_config()
root.mainloop()