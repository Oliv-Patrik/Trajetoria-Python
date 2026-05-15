from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Bem Vindo a Oficina do Diabo!</h1>"

@app.route("/psiquiatria")
def psico():
    return "<h1>Ala da Psiquiatria!</h1>"

