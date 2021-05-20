
# importando as bibliotecas necessárias
from flask import Flask, render_template, request
from wtforms import Form, TextField

bannedIPS = list()

# criei uma classe que irá gerar o formulário que obtem o IP a ser banido
class banIP(Form):
    name = TextField('Banir IP:')


# aqui eu criei uma instancia da classe Flask
app = Flask(__name__)
# e defino uma chave de segurança, ela não é usada mas é necessária para a execução livre de erros
app.config['SECRET_KEY'] = 'proof'


# definindo a rota principal, o diretorio raiz da nossa aplicação
@app.route("/", methods=['GET', 'POST'])
def root():
    # nesta linha eu crio também uma instancia 
    form = banIP(request.form)
    
    # analisa o tipo da request que foi realizada, e no caso de uma POST request o valor inserido no formulário
    if request.method == 'POST':
        name = request.form['name']
        bannedIPS.append(name)
    
    # retorna o html da pasta templates e executa ele
    return render_template('index.html', form=form)


@app.route("/listagem")
def listIP():
    return str(bannedIPS)


def returnBans():
    return bannedIPS

# e por fim roda o nosso código
app.run()