# Executando o primeiro olá mundo no TKINTER do Python
# É importante citar que tudo que acontece na janela do Tkinter é um elemento gráfico (widget), desde a abertura de janela até as informações internas
# Para que as informações seja inseridas na janela, basta inserir as informações no bloco de código do Tkinter
# Componentes no Tkinter são chamados de widgets, contendo rótulos
# Os widgets precisam ficar posicionados entre o root e o root.mainloop
# Criando a janela principal da aplicação
# Essa aplicação gera uma janela em branco, sendo esta a janela padrão
# O primeiro parametro de um widget sempre será a página no qual eles estarão posicionados

import tkinter as tk # Importando o módulo gráfico tkinter e adicionando um apelido para ele

# Por convenção a janela principal do TKINTER tem o nome de root
root = tk.Tk() ## Classe TK representa a janela principal da aplicação.

lbl = tk.Label(root,text ='Olá mundo!') # Esse é um objeto do tipo rótulo, a informação que queremos que apareça na aplicação.
lbl.pack() # O metodo pack é o responsável por exibir a informação na aplicação, sendo um metodo de posicionamento

root.mainloop() # É preciso ser criado, por que ela que mantem a aplicação funcionando ## É loop de eventos principais da aplicação. Ele contem todos os sub lopps da aplicação