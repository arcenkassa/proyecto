from flask import Flask
from flask import render_template
from mongoengine import *
from flask_mongoengine import MongoEngine


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hola amigos de Geeky Theory!'

@app.route('/inicio')
def inicio():
    palabra={'nombre':'asd','nombre1':'asd','nombre2':'arcen','titulo':'principal'}
    return render_template('index.html',palabra=palabra)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
