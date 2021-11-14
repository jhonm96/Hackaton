import re
from sys import meta_path
from flask import Flask, request, render_template, redirect, session, jsonify
from werkzeug.security import generate_password_hash
from src.script.crear_tablas import crear_tablas
from src.service.Usuario import crear_usuario, obtener_usuario, crear_usuario_registro, obtener_usuario_cedula, actualizar_usuario
from src.service.Autenticacion import autenticacion_usuario
from src.service.Recuperar import recuperar_datos
from src.service.Restablecer import restablecer_password
from src.service.DatosDashboard import total_ventas, ventas_hoy, total_usuario, usuario_nuevos, obtener_usuario_nuevos
from src.service.Producto import crear_producto
from src.service.Listado import filtro_solo_rangoCompras
import ast


app = Flask(__name__)
app.secret_key = 'mi_llave_secreta'


autenticacion = ['dashboard', 'agregar_producto']
sinAutenticacion = ['login', 'registro', 'recuperar', 'restablecer']

@app.before_request
def antes_peticion():
    if 'usuario' not in session and request.endpoint in autenticacion:
        return redirect('/login')

    elif 'usuario' in session and request.endpoint in sinAutenticacion:
        return redirect('/dashboard')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form["email"]
        password = request.form["password"]

        usuario = autenticacion_usuario(email, password)

        if usuario:
            session['usuario'] = email
            if usuario.role == 'super admin':
                return redirect('/dashboard')
            elif usuario.role == 'usuario externo':
                return redirect('/')
            else:
                return 'usuario interno'        
        else:
            return redirect('/login')

@app.route('/dashboard')
def dashboard():
    _total_ventas = total_ventas()
    _ventas_hoy = ventas_hoy()
    _total_usuario = total_usuario()
    _usuario_nuevos = usuario_nuevos()

    usuario = obtener_usuario(session['usuario'])

    usuarios_nuevos = obtener_usuario_nuevos()


    return render_template('dashboard.html',  total_ventas =_total_ventas, ventas_hoy = _ventas_hoy, total_usuario = _total_usuario, usuario_nuevos = _usuario_nuevos, usuario = usuario, usuarios_nuevos = usuarios_nuevos)

@app.route('/registro_admin', methods=['GET', 'POST'])
def registro_admin():
    if request.method == 'GET':
        return render_template('registro_admin.html')
    else: 
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        sexo = request.form['sexo']
        fecha_nac = request.form['fecha_nac']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        cargo = request.form['cargo']
        email = request.form['email']
        password = request.form['password']

        crear_usuario_registro(cedula, nombre, sexo, fecha_nac, direccion, ciudad, email, generate_password_hash(password), cargo)

        return redirect('/dashboard')


@app.route('/recuperar', methods=['GET', 'POST'])
def recuperar():
    if request.method == 'GET':
        return render_template('recuperar_datos.html')
    else: 
        email = request.form['email']
        recuperar_datos(email)
        return redirect('/restablecer')

@app.route('/restablecer', methods=['GET', 'POST'])
def restablecer():
    if request.method == 'GET':
        return render_template('restablecer.html')
    else:
        password_anterior = request.form['password_anterior']
        password = request.form['password']
        ver_password = request.form['ver_password']
        restablecer_password(password_anterior, password, ver_password)
        return redirect('/login')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/usuario_admin')
def usuario_admin():
    return render_template('usuario_admin.html')

@app.route('/usuario/<cedula>')
def obtener_usuario_por_cedula(cedula):
    usuario = obtener_usuario_cedula(cedula)

    jsonstr = {'nombre': usuario.nombre, 'cedula': usuario.cedula, 'sexo': usuario.sexo, 'fecha_nac': usuario.fecha_nac, 'direccion': usuario.direccion, 'ciudad': usuario.ciudad, 'cargo': usuario.role }

    if usuario:
        return jsonify(jsonstr)
    else:
        return None

@app.route('/eliminar_usuario/<cedula>')
def eliminar_usuario_por_cedula(cedula):
    usuario = obtener_usuario_cedula(cedula)

    if usuario:
        usuario.delete_instance()
        return jsonify({'mensaje': 'usuario eliminado'})
    else:
        return None

@app.route('/actualizar_usuario/<cedula>', methods=['POST'])
def actualizar_usuario_por_cedula(cedula):
    usuario = obtener_usuario_cedula(cedula)

    if usuario:
        actualizar_usuario(usuario, ast.literal_eval(request.data.decode()))

        jsonstr = {
            'mensaje': 'usuario actualizado', 'nombre': usuario.nombre, 'cedula': usuario.cedula, 'sexo': usuario.sexo, 'fecha_nac': usuario.fecha_nac, 'direccion': usuario.direccion, 'ciudad': usuario.ciudad, 'cargo': usuario.role
        }

        return jsonify(jsonstr)
    else:
        return None

@app.route('/producto_admin')
def producto_admin():
    return render_template('producto_admin.html')

@app.route('/listados', methods = ['GET', 'POST'])
def listados():
    
    usuario = obtener_usuario(session['usuario'])

    if request.method == 'GET':
        return render_template('listados.html', usuario = usuario)
    else:
        rango_compras = request.form['rango_compras']
        rango_compras= rango_compras.split('-')
        if len(rango_compras)==2:   
            compra_inferior = rango_compras[0]
            compra_superior = rango_compras[1]
        elif len(rango_compras)==1:
            compra_inferior = '0'
            compra_superior = rango_compras[0]

        rango_bonos = request.form['rango_bonos']

        rango_bonos= rango_bonos.split('-')
        if len(rango_bonos)==2:   
            bono_inferior = rango_bonos[0]
            bono_superior = rango_bonos[1]
        elif len(rango_bonos)==1:
            bono_inferior = '0'
            bono_superior = rango_bonos[0]
        sexo = request.form['sexo']
        fecha_nac = request.form['fecha_nac']
        prod_esp = request.form['prod_esp']
        ciudad = request.form['ciudad']
        fecha_compra = request.form['fecha_compra']

        #listar solo por rango acum de compras
        if bono_inferior == '' and bono_superior == '' and sexo == '' and fecha_nac == '' and prod_esp == '' and ciudad == '' and fecha_compra == '':
            lista_usuarios = filtro_solo_rangoCompras(compra_inferior, compra_superior)

        return render_template('/listado', lista_usuarios = lista_usuarios)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'GET':
        return render_template('agregar_producto.html')
    else: 
        nombre = request.form['nombre']
        codigo = request.form['codigo']
        tipo_unidad = request.form['tipo_unidad']
        fecha_ingreso = request.form['fecha_ingreso']
        bono = request.form['bono']
        precio_unitario = request.form['precio_unitario']
        aplica_bono = request.form['aplica_bono']
        cantidad_estandar = request.form['cantidad_estandar']
        crear_producto(nombre, codigo, tipo_unidad, fecha_ingreso, bono, precio_unitario, aplica_bono, cantidad_estandar)
        return redirect('/dashboard')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        return render_template('registro.html')
    else:
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        sexo = request.form['sexo']
        fecha_nac = request.form['fecha_nac']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        email = request.form['email']
        password = request.form['password']

        password_encrypt = generate_password_hash(password)

        crear_usuario(cedula, nombre, sexo, fecha_nac, direccion, ciudad, email, password_encrypt)

        return redirect('/login')

@app.route('/cerrar_sesion')
def cerrar_sesion():
    if 'usuario' in session:
        session.pop('usuario')
        return redirect('/')

@app.route('/perfil')
def perfil():
    usuario = obtener_usuario(session['usuario'])
    return render_template('perfil.html', usuario = usuario)

@app.route('/administrarproducto')
def administrarproducto():
    return render_template('administrarproducto.html')

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/hola')
def hola():
    return 'hola'

if __name__ == '__main__':
    crear_tablas()
    app.run(debug=True)
    

