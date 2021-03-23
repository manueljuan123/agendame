from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'agendate'

mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', usuarios = data) 



@app.route('/login', methods=["POST"])
def login(cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx):
    email=request.form['email']
    contrasena=request.form['contrasena']

    try:
        cur=mysql.connection.cursor()
        cur.execute(f'SELECT * FROM usuario WHERE email = {email}')
        data = cur.fetchall()
        cur.close()
        return render_template('eventos.html', email = data[0])
    except:
        flash ("El usuario o la contraseña no son correctos. Revise o regístrese en la parte inferior, por favor")
        return render_template('index.html')
        


if __name__== "__main__":
    app.run(debug=True)

