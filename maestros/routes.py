
from . import maestros
from wtforms.validators import email
from config import DevelopmentConfig
from flask import Flask, render_template,request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect 
from flask import g
from models import db, Alumnos, Maestros
from flask_migrate import Migrate
#from maestros import maestros
import forms

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"


@maestros.route("/")
def lista():
	create_form=forms.UserForm(request.form)
	#ORM SELECT * FROM Maestros;
	maestro=Maestros.query.all()
	return render_template("maestros/listaMaestros.html", form=create_form, maestro=maestro)


@maestros.route("/agregar", methods=['GET','POST'])
def agregar():
      create_form=forms.UserForm(request.form)

      if request.method=='POST':
            maestro_existe=Maestros.query.filter_by(matricula=create_form.matricula.data).first()
            if maestro_existe:
                   return render_template("maestros/agregarM.html", form=create_form, errores={"matricula": ["La matricula ya esta registrada"]})
            
            mae=Maestros(matricula=create_form.matricula.data,
                         nombre=create_form.nombre.data,
                         apellidos=create_form.apellidos.data,
                         especialidad=create_form.especialidad.data,
                         email=create_form.email.data)
            db.session.add(mae)
            db.session.commit()
            return redirect(url_for('maestros.lista'))
      return render_template("maestros/agregarM.html", form=create_form)
            
@maestros.route("/modificar", methods=['GET', 'POST'])
def modificar():
      create_form=forms.UserForm(request.form)
      if request.method=='GET':
            matricula=request.args.get('matricula')

            mae=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
            create_form.matricula.data=matricula
            create_form.nombre.data=mae.nombre
            create_form.apellidos.data=mae.apellidos
            create_form.especialidad.data=mae.especialidad
            create_form.email.data=mae.email
            return render_template('maestros/modificarM.html', form=create_form)
      
      if request.method=='POST':
            matricula=create_form.matricula.data
            mae=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
            mae.nombre=str.rstrip(create_form.nombre.data)
            mae.apellidos=str.rstrip(create_form.apellidos.data)
            mae.especialidad=str.rstrip(create_form.especialidad.data)
            mae.email=str.rstrip(create_form.email.data)
            db.session.add(mae)
            db.session.commit()
            return redirect(url_for('maestros.lista'))

@maestros.route("/eliminar", methods=['GET','POST'])
def eliminar():
      create_form= forms.UserForm(request.form)
      if request.method=='GET':
            matricula= request.args.get('matricula')

            mae= db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
            if mae:
                  create_form.matricula.data=mae.matricula
                  create_form.nombre.data=mae.nombre
                  create_form.apellidos.data=mae.apellidos
                  create_form.especialidad.data=mae.especialidad
                  create_form.email.data=mae.email
                  return render_template("maestros/eliminarM.html", form=create_form)
            
      if request.method=='POST':
                  matricula=create_form.matricula.data
                  mae =db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
                  if mae:
                        db.session.delete(mae)
                        db.session.commit()
                        return redirect(url_for('maestros.lista'))

      return render_template("maestros/eliminarM.html", form=create_form)


@maestros.route("/detalles", methods=['GET','POST'])
def detalles():
       create_form=forms.UserForm(request.form)
       if request.method=='GET':
              matricula=request.args.get('matricula')
              mae=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
              matricula=request.args.get('matricula')
              nombre=mae.nombre
              apellidos=mae.apellidos
              especialidad=mae.especialidad
              email=mae.email
       return render_template("maestros/detallesM.html",
                               nombre=nombre, apellidos=apellidos,
                               especialidad=especialidad,email=email)