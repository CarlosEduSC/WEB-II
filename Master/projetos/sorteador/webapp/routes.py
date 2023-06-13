from flask import Flask, render_template
# importando a variavel app do __init__.py
from . import app

# era o main.py -> renomado para "routes.py"

# cria uma rota para: http://127.0.0.1:5000/index
@app.route("/index")
def index():
    return render_template('index.html')
    # return "<h1>Olá, tudo certo por aqui!</h1>"

@app.route("/gerar")
def gerar():
    # eh o onde a magica acontece...
    # gerar os numeros
    # e retorna os numero para a view (index.html)
    from random import randrange

    numeros = [11, 22, 33, 44, 55, 60]
    # executa 6 vezes de 0 a 5
    for c in range(0, 6):
        # rand gera os numero aleatoriamente (1 a 60)
        numeros[c] = randrange(1, 60)

    return render_template('index.html', numeros=numeros)

# outra rota: http://127.0.0.1:5000/logout
@app.route("/logout")
def logout():
    return "<h1>Adios!</h1>"

# para simular um request passando parametros
# http://127.0.0.1:5000/imc?peso=77&altura=1.55
@app.route("/imc")
def imc():
    # funcao para pegar parametros do formulario ou url
    from flask import request
    # get("name da input")
    # <input type='text' name='peso'>
    peso = float(request.args.get("peso"))
    altura = float(request.args.get("altura"))
    imc_calc = peso / (altura * altura)

    # if imc > 10:
    #    mensagem=""
    # if imc < 10:
    #    pass

    return f"seu imc é: {imc_calc}"
    # return f"seu peso é: {peso} | altura = {altura}"
    # return render_template('imc.html', numeros=numeros)

# MUITO, MAS MUITO IMPORTANTE!!!! ATIVAR O DEGUB
app.run(debug=True)
