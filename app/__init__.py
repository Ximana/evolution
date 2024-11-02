from flask import Flask, redirect, request

#importar outros arquivos

# Importar os modelos

# Importar os controladores
from .controllers.home_controller import home_bp

def create_app():
    app = Flask(__name__)
    
    #Registrar os blueprints
    app.register_blueprint(home_bp)

    return app
