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


@app.route('/eventos', methods=["POST","GET"])
def login():
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

            cur=mysql.connection.cursor()
            cur.execute('SELECT * FROM eventos')
            data = cur.fetchall()
            cur.close()
            return render_template('eventos.html', eventos = data)

        else:
            flash("Su usuario o contraseña no son correctos, vuelva a intentarlo o regístrese, por favor")
            return render_template('index.html')



@app.route('/registro', methods=["POST","GET"])       
def registro():
    if request.method == 'POST':
        nombreUsuario = request.form['nombreUsuario']
        apellidoUsuario = request.form['apellidoUsuario']
        edadUsuario = request.form['edadUsuario']
        ocupacion = request.form["ocupacion"]
        email = request.form["email"]
        contrasena = request.form["contrasena"]
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO usuario (nombreUsuario, apellidoUsuario, edadUsuario, ocupacion, email, contrasena) VALUES (%s,%s,%s,%s,%s,%s)',(nombreUsuario,apellidoUsuario,edadUsuario,ocupacion,email,contrasena)) 
        mysql.connection.commit()
        flash("Se ha registrado con éxito, gracias por elegirnos. Para confirmar, ingrese con los datos anteriormente digitados, por favor.")
        return redirect(url_for('index'))

    return render_template('registro.html')


@app.route('/evento',methods=["POST","GET"])
def insertEvent(id):
    if request.method == 'POST':
        titulo = request.form['title']
        descripcion = request.form['descripcion']
        hora = request.form['hora']
        fecha = request.form['fecha']
        lugar = request.form['lugar']
        cursor = mysql.connection.cursor()
        id=cursor.fetchone()
        if id:
            session['codEvento'] = id['codEvento']
            cursor.execute(F'INSERT INTO eventos (titulo, descripcion, hora, fecha, lugar, codEvento) VALUES ({titulo},{descripcion},{hora},{fecha},{lugar},{id})')
            mysql.connection.commit()
            data = cursor.fetchall()
            flash("Evento guardado con éxito")

            return render_template('index.html')







if __name__== "__main__":
    app.run(debug=True)

