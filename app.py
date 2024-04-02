from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configuração e conexão do banco de dados 
config = {
    'user': 'root', 
    'password': 'aula123', 
    'host': 'db', 
    'database': 'ac1',
    'raise_on_warnings': True
}

@app.route('/')
def index():
    return "Seja bem-vindo!"

@app.route('/iniciar')
def iniciar():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST' and 'nome' in request.form and 'email' in request.form and 'telefone' in request.form and 'endereco' in request.form:
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']

        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Inserindo os dados no banco
        query = "INSERT INTO usuarios(nome, email, telefone, endereco) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nome, email, telefone, endereco))
        cnx.commit()
        cursor.close()
        cnx.close()
        return "Usuário cadastrado"
    
    return render_template('cadastro.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')