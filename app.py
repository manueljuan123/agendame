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

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        correo=request.form.get('email')
        password=request.form.get('contrasena')
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT idUsuario, contrasena FROM usuario WHERE email = '{correo}'")
        
        usuario= cursor.fetchone()
        if usuario is None:
            flash("Su datos son incorrectos")
            return redirect(url_for('index'))
            
        
        if usuario[1]==password:
            session['login']=usuario[0]
            return redirect(url_for('login'))
            
        else:
            flash("Su contraseña es incorrectos")
            return redirect(url_for('index'))

@app.route('/eventos', methods=["POST","GET"])
def login():
    if not 'login' in session:
        return redirect(url_for('index'))
    if request.method=='GET':
        curso = mysql.connection.cursor()
        id_usuario = session['login']
        curso.execute(f"SELECT * FROM eventos WHERE codEvento = {id_usuario}")
        data = curso.fetchall()
        return render_template('eventos.html', eventos = data)
        


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
        cursor.execute(f"SELECT idUsuario FROM usuario WHERE email = '{email}'")
        id = cursor.fetchone()
        session['login']=id[0]
        return redirect(url_for('login'))

    return render_template('registro.html')


@app.route('/evento',methods=["POST","GET"])
def insertEvent():
    if not 'login' in session:
        flash("debe iniciar session")
        return render_template('index.html')
    if request.method == 'POST':
        id_usuario = session['login']
        descripcion = request.form.get ('descripcion')
        hora = request.form.get ('hora')
        fecha = request.form.get ('fecha')
        lugar = request.form.get ('lugar')
        cursor = mysql.connection.cursor()
        
        cursor.execute('INSERT INTO eventos (descripcion, hora, fecha, lugar, codEvento) VALUES (%s,%s,%s,%s,%s)',(descripcion,hora,lugar,fecha,id_usuario))
        mysql.connection.commit()
            
        flash("Evento guardado con éxito")

        return redirect(url_for('login'))
    

@app.route("/salir")
# Funcion para salir
def salir():
    session.clear()
    return redirect(url_for('index'))



if __name__== "__main__":
    app.run(debug=True)

