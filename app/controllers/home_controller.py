
from flask import render_template, Blueprint

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')

@home_bp.route('/sobre')
def sobre():
    return render_template('sobre.html')
   
@home_bp.route('/projectos')
def projectos():
    return render_template('index.html')
   
@home_bp.route('/noticias')
def noticias():
    return render_template('index.html')
   
@home_bp.route('/biblioteca')
def biblioteca():
    return render_template('index.html')
   
@home_bp.route('/galeria')
def galeria():
    return render_template('index.html')
    
@home_bp.route('/procura')
def procura():
    return render_template('index.html')
   
@home_bp.route('/networking')
def networking():
    return render_template('index.html')
   

   

