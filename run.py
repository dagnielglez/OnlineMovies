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
#INSTALAR PYMYSQL EN EL ENTORNO VIRTUAL
#ACTIVA EL ENTORNO VIRTUAL Y: pip install pymysql
#COMPILA LA PAGINA: python run.py
#FINALIZA AGREGANDO AL REPOSTORIO: git add .
#CREA UN COMMIT: git commit -m "Hemos conectado base de datos"
#Y guarda todo en la rama maestra: git push -u origin master

#Puedes confirmar en la pagina dde github si se han guardado los cambios