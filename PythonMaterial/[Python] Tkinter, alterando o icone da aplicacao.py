# Como alterar o icone da aplicação
# O arquivo precisa estar no formato .ico
import tkinter as tk

root = tk.Tk()
root.title('Alterando o icone da aplicação')

window_width = 600
window_heigh = 300

center_x = int(root.winfo_screenwidth()/2 - window_width/2)
center_y = int(root.winfo_screenheight()/2 - window_heigh/2)

root.geometry(f'{window_width}x{window_heigh}+{center_x}+{center_y}')

# Modelo de alteração de icone, utilizando o metodo ICONBITMAP
root.iconbitmap('C:\\Users\\Raul\\Downloads\\Icone.ico')

root.mainloop()