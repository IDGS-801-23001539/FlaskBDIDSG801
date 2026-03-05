from . import alumnos
from wtforms.validators import email
from config import DevelopmentConfig
from flask import Flask, render_template,request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect 
from flask import g
from models import db, Alumnos
from flask_migrate import Migrate
import forms


@alumnos.route("/")
def listaAlumnos():
	create_form=forms.UserForm2(request.form)
	#ORM SELECT * FROM Alumnos;
	alumno=Alumnos.query.all()
	return render_template("alumnos/index.html", form=create_form, alumno=alumno)


@alumnos.route("/agregarA", methods=['GET','POST'])
def agregarAlumno():
	create_form=forms.UserForm2(request.form)

	if request.method=='POST':

		alum=Alumnos(nombre=create_form.nombre.data,
			   apellidos=create_form.apellidos.data,
			   email=create_form.email.data,
			   telefono=create_form.telefono.data)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('alumnos.listaAlumnos'))
	
	return render_template("alumnos/agregarA.html", form=create_form)


@alumnos.route('/detallesA', methods=['GET','POST'])
def detallesAlumno():
	create_form=forms.UserForm2(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		#select * from alumnos where id==id
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		id=request.args.get('id')
		#print(alum1.nombre + alum1.apaterno + alum1.email)
		nombre=alum1.nombre
		apellidos=alum1.apellidos
		email=alum1.email
		telefono=alum1.telefono
	return render_template('alumnos/detalles.html', nombre=nombre, apellidos=apellidos, email=email, telefono=telefono)

@alumnos.route("/modificarA", methods=['GET','POST'])
def modificarAlumno():
	create_form=forms.UserForm2(request.form)
	if request.method=='GET':
		id=request.args.get('id')

		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()

		create_form.id.data=id
		create_form.nombre.data=alum1.nombre
		create_form.apellidos.data=alum1.apellidos
		create_form.email.data=alum1.email
		create_form.telefono.data=alum1.telefono

		return render_template('alumnos/modificar.html', form=create_form)
	
	if request.method=='POST':
		id=create_form.id.data
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alum1.nombre=str.rstrip(create_form.nombre.data)
		alum1.apellidos=str.rstrip(create_form.apellidos.data)
		alum1.email=str.rstrip(create_form.email.data)
		alum1.telefono=str.rstrip(create_form.telefono.data)
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for('alumnos.listaAlumnos'))

@alumnos.route('/eliminarA', methods=['GET','POST'])
def eliminarAlumno():
	create_form = forms.UserForm2(request.form)
	if request.method== 'GET':
		id = request.args.get('id')
		alum1= db.session.query(Alumnos).filter(Alumnos.id==id).first()
		if alum1:
			create_form.id.data=alum1.id
			create_form.nombre.data= alum1.nombre
			create_form.apellidos.data=alum1.apellidos
			create_form.email.data=alum1.email
			create_form.telefono.data=alum1.telefono
			return  render_template("alumnos/eliminar.html", form=create_form)
	
	if request.method=='POST':
		id=create_form.id.data
		alumn = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		if alumn:
			db.session.delete(alumn)
			db.session.commit()
			return redirect(url_for('alumnos.listaAlumnos'))
	
	return render_template("alumnos/eliminar.html", form=create_form)
		