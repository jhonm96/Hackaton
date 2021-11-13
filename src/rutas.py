from wtforms import form
from app import app
from flask import render_template, redirect, request
from flask import Flask, render_template, redirect, session, flash, request, send_file
from flask.helpers import make_response, url_for
from markupsafe import escape
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import yagmail


#Inicio

@app.route('/')
def inicio():
    var = "inicio"
    return render_template('prueba.html', var=var)

@app.route('/login')
def login():
    var = "login"
    return render_template('prueba.html', var=var)

@app.route('/recuperar')
def recuperar():
    var = "recuperar contraseña"
    email="jsaboya@uninorte.edu.co"
    yag = yagmail.SMTP('misionticuninorte@gmail.com', 'Mi$ionTic2022') 
    yag.send(to=email, subject='Recupera tu contraseña',
    contents='Bienvenido,\n a continuación te presento tu información para que puedas iniciar sesión:\n antiguo password : prueba\ningresa en este link:\nhttp://127.0.0.1:5000/reestablecer')
    flash('Revisa tu correo para activar tu cuenta')  
    return render_template('prueba.html', var=var)

@app.route('/reestablecer')
def reestablecer():
    var = "reestablecer contraseña"
    return render_template('prueba.html', var=var)

@app.route('/registro')
def registro():
    var = "registro externo"
    return render_template('prueba.html', var=var)

@app.route('/buscar')
def buscar():
    var = "buscar producto"
    return render_template('prueba.html', var=var)


# Usuario

@app.route('/user/verproducto')
def verproducto():
    var = "ver el producto  "
    return render_template('prueba.html', var=var)

@app.route('/user/listaf')
def listaf():
    var = "lista de compra y deseos"
    return render_template('prueba.html', var=var)

@app.route('/user/listadeseos')
def listadeseo():
    var = "lista de deseos"
    return render_template('prueba.html', var=var)

@app.route('/user/listacompras')
def listacompra():
    var = "lista de compras"
    return render_template('prueba.html', var=var)


# Admin

@app.route('/admin/home')
def adminhome():
    var = "admin home"
    return render_template('prueba.html', var=var)

@app.route('/admin/registro')
def adminregistro():
    var = "admin registro"
    return render_template('prueba.html', var=var)

@app.route('/admin/productos')
def adminproductos():
    var = "admin productos"
    return render_template('prueba.html', var=var)

@app.route('/admin/productos-gestion')
def adminproductosgestion():
    var = "admin productos actualizar o eliminar"
    return render_template('prueba.html', var=var)

@app.route('/admin/productos-agregar')
def adminproductosagregar():
    var = "admin agregar productos"
    return render_template('prueba.html', var=var)

@app.route('/admin/clientes')
def adminclientes():
    var = "admin clientes"
    return render_template('prueba.html', var=var)

@app.route('/admin/usuarios')
def adminusuarios():
    var = "admin usuarios"
    return render_template('prueba.html', var=var)

@app.route('/admin/listados-clientes')
def adminlisclientes():
    var = "admin listados de clientes"
    return render_template('prueba.html', var=var)

# Error

@app.errorhandler(404)
def error404(error):
    try:
        var = "error 404"
        return render_template('prueba.html', var=var)
    except:
        var = "error fatal"
        return render_template('prueba.html', var=var)

