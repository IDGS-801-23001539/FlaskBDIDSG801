from . import cursos

from wtforms.validators import email
from config import DevelopmentConfig
from flask import Flask, render_template,request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect 
from flask import g
from models import db, Curso ,Maestros
from flask_migrate import Migrate
#from maestros import maestros
import forms


@cursos.route("/")
def listaCursos():
    create_form=forms.UserForm3(request.form)
    curso=Curso.query.all()
    return render_template("cursos/listaCursos.html", form=create_form, curso=curso)

@cursos.route("/agregarC", methods=['GET', 'POST'])
def agregarCurso():
    create_form=forms.UserForm3(request.form)
    maestros = Maestros.query.all()

    create_form.id_maestro.choices = [(m.matricula, m.nombre) for m in maestros]

    if request.method=='POST':
        cur=Curso(nombre=create_form.nombre.data,
                   descripcion=create_form.descripcion.data,
                   maestro_id=create_form.id_maestro.data)
        db.session.add(cur)
        db.session.commit()
        return redirect(url_for('cursos.listaCursos'))
    return render_template("cursos/agregarC.html", form=create_form)

@cursos.route("/modificarC", methods=['GET','POST'])
def modificarCurso():
    create_form=forms.UserForm3(request.form)
    maestros = Maestros.query.all()

    create_form.id_maestro.choices = [(m.matricula, m.nombre) for m in maestros]


    if request.method=='GET':
        id=request.args.get('id')
        cur=db.session.query(Curso).filter(Curso.id==id).first()

        create_form.id.data=id
        create_form.nombre.data=cur.nombre
        create_form.descripcion.data=cur.descripcion
        create_form.id_maestro.data=cur.maestro_id

        return render_template("cursos/modificarC.html", form=create_form)
    
    if request.method=='POST':
        id=create_form.id.data
        cur=db.session.query(Curso).filter(Curso.id==id).first()
        cur.nombre=str.rstrip(create_form.nombre.data)
        cur.descripcion=str.rstrip(create_form.descripcion.data)
        cur.maestro_id=create_form.id_maestro.data
        db.session.add(cur)
        db.session.commit()
        return redirect(url_for('cursos.listaCursos'))
    
@cursos.route('/detallesC', methods=['GET'])
def detallesCurso():

    id = request.args.get('id')

    cur = db.session.query(Curso).filter(Curso.id == id).first()
    maestro = db.session.query(Maestros).filter(Maestros.matricula == cur.maestro_id).first()


    nombre = cur.nombre
    descripcion = cur.descripcion
    
    return render_template('cursos/detallesC.html',
        nombre=nombre,
        descripcion=descripcion,
        maestro=maestro
    )   

@cursos.route('/eliminarC', methods=['GET','POST'])
def eliminarCurso():
	create_form = forms.UserForm3(request.form)
	if request.method== 'GET':
		id = request.args.get('id')
		cur= db.session.query(Curso).filter(Curso.id==id).first()
		if cur:
			create_form.id.data=cur.id
			create_form.nombre.data= cur.nombre
			create_form.descripcion.data=cur.descripcion
			create_form.id_maestro.data=cur.maestro_id
			
			return  render_template("cursos/eliminarC.html", form=create_form)
	
	if request.method=='POST':
		id=create_form.id.data
		cur = db.session.query(Curso).filter(Curso.id==id).first()
		if cur:
			db.session.delete(cur)
			db.session.commit()
			return redirect(url_for('cursos.listaCursos'))
	
	return render_template("cursos/eliminarC.html", form=create_form)

@cursos.route("/alumnosCurso/<int:id>")
def alumnosCurso(id):

    curso = Curso.query.get(id)

    return render_template(
        "cursos/alumnosCurso.html",
        curso=curso,
        alumnos=curso.alumnos
    )