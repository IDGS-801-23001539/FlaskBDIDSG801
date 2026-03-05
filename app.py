from wtforms.validators import email
from config import DevelopmentConfig
from flask import Flask, render_template,request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect 
from flask import g
from models import db, Alumnos, Maestros
from flask_migrate import Migrate
from maestros import maestros
from alumnos import alumnos
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros,url_prefix="/maestros")#registra el blueprint de maestros
app.register_blueprint(alumnos)

csrf=CSRFProtect()
db.init_app(app)
migrate=Migrate(app,db)



# Manejador de error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404





	


if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(debug=True)
