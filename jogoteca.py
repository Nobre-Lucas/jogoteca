from flask import Flask, render_template, request, redirect, session, flash, url_for


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
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Somente usuários logados podem registrar novos jogos')
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categorias = request.form['categorias']
    consoles = request.form['consoles']
    jogo = Jogo(nome, categorias, consoles)
    lista_de_jogos.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima_pagina = request.args.get('proxima')
    return render_template('login.html', proxima=proxima_pagina)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mellon' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f'Usuário {session["usuario_logado"]} logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado!')
        return redirect(url_for('login'))
    

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
