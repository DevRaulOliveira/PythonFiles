# Definindo o estado inicial da janela da aplicação
# Metodo STATE
# Metodo STATE('zoomed') -> maximizada e STATE('iconic') -> Minimizada
# Metodo STATE retorna o estado atual da janela da aplicação

import tkinter as tk

root = tk.Tk()
root.title('Definindo o estado inicial da janela')
root.geometry('600x400+300+200')
root.resizable(1,1) # Os valores no resizable são booleanos, podendo ser true ou false (1 ou 0)


# Apresentando a janela de forma maximizada utilizando o metodo STATE('ZOOMED')
root.state('zoomed') # 'zoomed' permite apresentar a janela da aplicação maximizada

# Apresentando a janela da aplicação de forma minimizada utilizando STATE('ICONIC')
root.state('iconic') # 'iconic' permite que ao iniciar a aplicação comece minimizada

# Apresentando a janela da aplicação no tamanho normal, usando STATE('normal')
root.state('normal')

# Apresentando o estado atual da aplicação
root.state() # Desta forma é retornado o estado atual da aplicação
root.mainloop()
