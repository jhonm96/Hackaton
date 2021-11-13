from flask import Flask, render_template, request, redirect, session
import Modelo, sys
import werkzeug.security as ws

# sys.setrecursionlimit(9999)



app = Flask(__name__)

paginasConAutenticacion = ['home']
paginasSinAutenticacion = ['login', 'registro']

@app.before_request
def before_request():
    if 'usuario' not in session and request.endpoint in paginasConAutenticacion:
        return redirect('/login')
    if 'usuario' in session and request.endpoint in paginasSinAutenticacion:
        return redirect('/home')



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    Modelo.registroProducto('producto_X', 'inventario_x', 'bolsa', 1500, 0)
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        return render_template('registro.html')
    else:
        username = request.form['username']
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        sexo = request.form['sexo']
        fechaNacimiento = request.form['fecha_nac']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        password = request.form['password']
        ver_password = request.form['ver_password']
        
        if password == ver_password:
            Modelo.registrar(username, password, email, nombre, apellido, cedula, sexo, fechaNacimiento, direccion, ciudad)
            return redirect('/login')
        else:
            return render_template('registro.html')
        
if __name__ == '__main__':
    app.run(debug=True, port='8000')
    Modelo.crearTablas()

    