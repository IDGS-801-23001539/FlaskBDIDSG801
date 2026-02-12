from flask import Flask, render_template
from flask import flash
from flask_wtf.csrf import CSRFProtect 
from flask import g


app = Flask(__name__)
csrf=CSRFProtect()



@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")


# Manejador de error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
	return render_template("alumnos.html")

if __name__ == '__main__':
	app.run(debug=True)
