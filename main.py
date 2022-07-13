
from flask import Flask, render_template

class jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = jogo('God of War', 'Ação', 'Playstation')
jogo2 = jogo('CS:Go', 'Tiro', 'PC')
jogo3 = jogo('Minecraft', 'Construção', 'PC')

lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos=lista)

app.run()