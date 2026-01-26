from flask import Flask
import random

app = Flask(__name__)

facts_list = ['A maioria das pessoas que sofre de dependência tecnológica sente um forte estresse quando fica fora da área de cobertura de rede ou não pode usar seus dispositivos',
'De acordo com um estudo realizado em 2018, mais da metade das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.',

'O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna',
'Segundo um estudo de 2019, mais de 60 porcento das pessoas respondem a mensagens de trabalho em seus smartphones dentro de 15 minutos após sair do trabalho',

'Uma forma de combater a dependência tecnológica é buscar atividades que tragam prazer e melhorem o humor']

@app.route("/")
def hello_world():
    return (f"<h1>Olá, nessa página você encontrará curiosidades sobre dependência tecnológica, aproveite!</h1> \n <a href='/random_facts'> Clique aqui e veja uma curiosidade aleatória!</a>")

@app.route("/random_facts")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/imagem")
def meme():
    return f'<img src = "https://miro.medium.com/1*GI-td9gs8D5OKZd19mAOqA.png" alt = "homem confuso" width ="400" height = "400">'

app.run(debug=True)

