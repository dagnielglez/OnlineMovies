#Import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config#importamos el archibo de configuracion config.py

#Instancias

app = Flask(__name__)
app.config.from_object(config)#esta configuracion debe ir primero q la de SQLALchemy o dara un error
db = SQLAlchemy(app)

#Rutas

@app.route('/')
def inicio():
    return ("Hola esta es la pagina de inicio")

if __name__ == '__main__':
    app.run(debug=True)
