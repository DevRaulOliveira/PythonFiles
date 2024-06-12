# Tkinter, tamanho e localização da janela
# Esses parametros são definidos com base em geometria, utilizando pixels como unidade de medida
# Width - Largura da janela
# Height - Altura da janela
# Y é a distancia da aplicação em relação a borda superior da tela
# X é a distancia da aplicação em relação a borda lateral da tela
# Caso não seja definido, será aplicada a medida padrão
# Utilizando valores negativos, muda a referencia
# Modelo de geometry = ('AlturaxLargura+Distancia do topo da tela + distancia do lado esquerdo da tela)

import tkinter as tk

root = tk.Tk()

root.title('Alterando altura, largura e posição da janela')

# Utilizando o metodo GEOMETRY e seu modelo

root.geometry('600x400+100+300') # Metodo utilizado para alterar as dimensões da janela
                # neste caso a janela da aplicação terá as dimensões 600 pixels de altura e 400 de largura
lblk = tk.Label(root,text='As dimensões da aplicação são 600 altura, 400 largura.\n100 Pixels de distancia da esquerda da tela e 300 pixels de distancia da borda superior')
lblk.pack()

root.mainloop()