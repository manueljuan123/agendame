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
            return render_template('eventos.html')

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

    return render_template('/registro.html')


@app.route('/idevento',methods=["POST","GET"])
def insertEvent(id):
    if request.method == 'POST':
        title = request.form['title']
        descripcion = request.form['descripcion']
        hora = request.form['hora']
        fechaInicio = request.form['fecha']
        fechaFinal = request.form['fechaFinal']
        lugar = request.form['lugar']
        color = request.form['color']
        textcolor = request.form['textcolor']

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO eventos (title, descripcion, hora, fecha, fechaFinal, lugar, color, textcolor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(title, descripcion, hora, fechaInicio, fechaFinal, lugar, color, textcolor))
        mysql.connection.commit()
        flash("Evento guardado con éxito")
        return redirect(url_for('eventos'))






if __name__== "__main__":
    app.run(debug=True)

