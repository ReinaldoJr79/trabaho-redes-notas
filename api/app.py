import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
app.config['DATABASE'] = 'banco.db'
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

def criar_tabela_notas():
    db = conectar_bd()
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT
    )
    ''')
    db.commit()
    db.close()

criar_tabela_notas()

@app.route('/cadastrar-nota', methods=['POST'])
def cadastrar_nota():
    if request.method == 'POST':
        data = request.get_json()
        titulo = data.get('titulo')

        emoji_response = requests.get('http://server-emoji:5001/emoji-aleatorio')
        emoji_data = emoji_response.json()
        emoji = emoji_data.get('emoji')

        mensagem = emoji + " - " + titulo

        db = conectar_bd()
        cursor = db.cursor()
        cursor.execute("INSERT INTO notas (titulo) VALUES (?)", (mensagem,))
        db.commit()
        db.close() 

        return "Nota inserida!"
    else:
        return "Método não suportado. Use POST para cadastrar uma nota."


@app.route('/notas', methods=['GET'])
def listar_notas():
    if request.method == 'GET':
        db = conectar_bd()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM notas")
        notas = cursor.fetchall()
        db.close()  

        return jsonify(notas)
    else:
        return "Método não suportado. Use GET para listar notas."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
