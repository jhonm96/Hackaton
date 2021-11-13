from flask import Flask
from src.scripts.crear_basedatos import crear_tablas
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    crear_tablas()