# Alterando a transparencia da janela da aplicação
# Metodo ATRIBUTES, utiliza dois parametros. O primeiro é o atributo que iremos alterar e segundo o valor do atributo
# '-alpha' representa o canal que cuida da transparencia da aplicação, variando de 0.0(transparente) e 1.0(nenhuma transparencia)

import tkinter as tk

root = tk.Tk()
root.title('Alterando a transparencia da janela da aplicação')
root.geometry('600x400+300+200')

# Modelo de alteração de transparencia de aplicação utilizando metodo ATTRIBUTES
root.attributes('-alpha', 0.5) # Alterando a transparencia da janela utilizando o canal alpha seguido do valor do canal


root.mainloop()