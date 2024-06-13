# Redimensionamento de aplicações e janelas
# Metodo resizeble, permite que seja manipulado a altura e largura da janela
# Metodo minsize e maxsize, definem os valores minimos e máximos de dimensionamento da janela da aplicação.

import tkinter as tk

root = tk.Tk()

root.title('Redimensionamento de aplicacoes')
root.geometry('600x400+500+200') # Medida padrão do tamanho da janela

# Modelo de redimensionamento de janelas usando o metodo RESIZE
root.resizable(True,True) # Define se a janela pode ser redimensionada na altura e na largura, neste parametro voce pode bloquear o redimensionamento da janela

# Modelo de bloqueio de redimensionamento de janelas
# root.resizable(False,False) # Lembrando que o primeiro parametro é a largura e o segundo para metro é a altura

# Limitando o redimensionamento da janela usando MINSIZE
root.minsize(300,200) # Tamnho minimo da janela é de 300 pixels de largura por 200 pixels de altura
root.maxsize(800,700) # Tamanho máxido da janela é de 800 pixels de largura por 700 pixels de altura


root.mainloop()