from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

# Atualize o caminho do banco de dados
DATABASE = '/app/db/database.sqlite'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL)''')
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
            conn.commit()
        return f"Recebido: {nome}, {email}"
    return render_template('form.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5002)
