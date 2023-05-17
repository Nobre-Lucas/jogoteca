from flask import Flask, render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, nome, categorias, consoles) -> None:
        self.nome = nome
        self.categorias = categorias
        self.consoles = consoles


app = Flask(__name__)
app.secret_key = 'lotr'

lista_de_jogos = []


@app.route('/')
@app.route('/home')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categorias = request.form['categorias']
    consoles = request.form['consoles']
    jogo = Jogo(nome, categorias, consoles)
    lista_de_jogos.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mellon' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f'Usuário {session["usuario_logado"]} logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado!')
        return redirect('/login')
    

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
