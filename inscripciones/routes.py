from . import inscripciones
from wtforms.validators import email
from config import DevelopmentConfig
from flask import Flask, render_template,request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect 
from flask import g
from models import db, Inscripciones,Alumnos, Curso
from flask_migrate import Migrate
import forms



@inscripciones.route("/")
def listaInscripciones():

    inscripciones = db.session.query(
        Inscripciones,
        Alumnos,
        Curso
    ).join(
        Alumnos, Inscripciones.alumno_id == Alumnos.id
    ).join(
        Curso, Inscripciones.curso_id == Curso.id
    ).all()

    return render_template(
        "inscripciones/listaInscripciones.html",
        inscripciones=inscripciones
    )
@inscripciones.route("/agregarIns", methods=['GET','POST'])
def agregarInscripciones():

    create_form = forms.InscripcionesForm(request.form)
    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()

    create_form.alumno_id.choices = [(a.id,f"{a.id} - {a.nombre} {a.apellidos}") for a in alumnos]
    create_form.curso_id.choices = [(c.id, c.nombre) for c in cursos]

    if request.method == 'POST':

        curso = Curso.query.get(create_form.curso_id.data)
        alumno = Alumnos.query.get(create_form.alumno_id.data)
        if alumno not in curso.alumnos:
            curso.alumnos.append(alumno)
            db.session.commit()
        else:
            flash("Este alumno ya está inscrito en ese curso")
        return redirect(url_for('inscripciones.listaInscripciones'))

    return render_template("inscripciones/agregarIn.html", form=create_form)

@inscripciones.route("/modificarIns", methods=['GET','POST'])
def modificarInscripciones():
    create_form=forms.InscripcionesForm(request.form)
    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()

    create_form.alumno_id.choices = [(a.id,f"{a.id} - {a.nombre} {a.apellidos}") for a in alumnos]
    create_form.curso_id.choices = [(c.id, c.nombre) for c in cursos]

    if request.method=='GET':
        id=request.args.get('id')
        ins=db.session.query(Inscripciones).filter(Inscripciones.id==id).first()

        create_form.id.data=id
        create_form.alumno_id.data=ins.alumno_id
        create_form.curso_id.data=ins.curso_id
        return render_template("inscripciones/modificarIns.html", form=create_form)

    if request.method=='POST':
        id=create_form.id.data
        ins=db.session.query(Inscripciones).filter(Inscripciones.id==id).first()
        alumno_id=create_form.alumno_id.data
        curso_id=create_form.curso_id.data

        existeIns=Inscripciones.query.filter(
            Inscripciones.alumno_id == alumno_id,
            Inscripciones.curso_id == curso_id,
            Inscripciones.id != id).first()
        if existeIns:
            flash("Este alumno ya está inscrito en ese curso")
            return redirect(url_for('inscripciones.listaInscripciones'))

        ins = Inscripciones.query.get(id)
        ins.alumno_id = alumno_id
        ins.curso_id = curso_id
        
        db.session.commit()
        return redirect(url_for('inscripciones.listaInscripciones'))

@inscripciones.route("/detallesIns")
def detallesInscripciones():

    id = request.args.get('id')

    ins = Inscripciones.query.get(id)

    curso = Curso.query.get(ins.curso_id)
    alumno = Alumnos.query.get(ins.alumno_id)

    return render_template(
        "inscripciones/detallesIns.html",
        alumno=alumno,
        curso=curso
    )

@inscripciones.route('/eliminarIns', methods=['GET','POST'])
def eliminarInscripciones():
    create_form = forms.InscripcionesForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        ins = db.session.query(Inscripciones).filter(Inscripciones.id == id).first()

        if ins:
            create_form.id.data = ins.id
            create_form.alumno_id.data = ins.alumno_id
            create_form.curso_id.data = ins.curso_id
            return render_template("inscripciones/eliminarIns.html", form=create_form)

    if request.method == 'POST':
        id = create_form.id.data
        ins = db.session.query(Inscripciones).filter(Inscripciones.id == id).first()
        if ins:
            db.session.delete(ins)
            db.session.commit()

            return redirect(url_for('inscripciones.listaInscripciones'))

    return render_template("inscripciones/eliminarIns.html", form=create_form)
