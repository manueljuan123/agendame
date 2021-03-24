from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_mysqldb import MySQL
import os
import re
import MySQLdb.cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'agendate'

mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["POST","GET"])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'contrasena' in request.form:
        idUsuario = request.form['email']
        idContrasena = request.form['contrasena']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuario WHERE email= %s AND contrasena= %s',(idUsuario,idContrasena))
        cuenta = cursor.fetchone()

        if cuenta:
            session['loggedin'] = True
            session['email'] = cuenta['email']
            session['contrasena'] = cuenta['contrasena']
            msg = "Logged in successfully!"
            return render_template('eventos.html', msg = msg)
        else:
            msg = "Incorrect username/password"
            return render_template('index.html', msg = msg)

        


if __name__== "__main__":
    app.run(debug=True)

