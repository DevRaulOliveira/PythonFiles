# Metodo TITLE, utiliza os argumentos inseridos como titulo da barra da aplicação

import tkinter as tk

root = tk.Tk() # Objeto da janela principal da classe Tk
# Propriedade TITLE, permite a mudança de titulo
root.title('Aplicação em execução') # Esse é o novo titulo da barra da aplicação

titulo = root.title() # Atribui o titulo da barra da aplicação a uma variável
lbl = tk.Label(root,text=titulo) # Esse etapa converte essa informação em uma label
lbl.pack() # Atribui o conteudo da Label a um pato dentro da aplicação, fazendo com que o titulo seja exibido dentro da aplicação.



root.mainloop() # Responsável por monitorar todas as ações da janela


