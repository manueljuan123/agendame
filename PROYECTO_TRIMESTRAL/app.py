from flask import Flask, render_template, request, redirect, url_flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DATABASE'] = ''

mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts=data)

@app.route('/registrar_usuario', methods=['POST'])
def reg_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['apellido']
        ocupacion = request.form['ocupacion']
        email = request.form['email']
        contraseña = request.form['contraseña']

