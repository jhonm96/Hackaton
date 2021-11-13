from flask import Flask
import Modelo
# from Modelo import Usuario, Producto, crearTablas


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    Modelo.crearTablas()
    app.run(debug=True, host='80')

    