from flask import render_template, redirect, url_for, current_app, request, abort
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app.models import MyFilms, MyRooms, Proyections
import werkzeug
from app.auth.decorators import admin_required

import os
from . import admin_bp
from .forms import FilmForm, UserAdminForm, RoomsForm, ProyectionsForm
import datetime


@admin_bp.route("/admin/")
@login_required
@admin_required
def index():
    page = int(request.args.get('page', 1))
    per_page = current_app.config['ITEMS_PER_PAGE']
    myfilm = MyFilms.all_paginated(page, per_page)
    return render_template("admin/index.html", myfilms=myfilm)
    

@admin_bp.route("/admin/<int:film_id>/")
@login_required
@admin_required
def show_films(film_id):
    myfilm = MyFilms.get_by_id(film_id)
    return render_template("admin/show_film.html", films=myfilm)


#--------------------------------------------------------------#
#---------------------------  FILMS  --------------------------#
@admin_bp.route("/admin/create/film", methods=['GET', 'POST'])
@login_required
@admin_required
def add_films():
    form = FilmForm()
    error = None
    if form.validate_on_submit():
        title = form.title.data 
        category = form.category.data
        premiere = form.premiere.data
        synopsis = form.synopsis.data
        file = form.film_image.data
        image_name = None
        myfilm = MyFilms.get_by_filmname(title)
        if myfilm is not None:
            error = f'El titulo {title} ya está en uso'
        else:
            if file:
                image_name = secure_filename(file.filename)
                images_dir = current_app.config['FILMS_IMAGES_DIR']
                os.makedirs(images_dir, exist_ok=True)
                file_path = os.path.join(images_dir, image_name)
                file.save(file_path)
            myfilm = MyFilms(
                user_id=current_user.id, film_title=title, 
                film_opening=premiere, film_category=category, 
                film_synopsis=synopsis)
            myfilm.film_image = image_name
            myfilm.save()
            return redirect(url_for('admin.index'))
    return render_template("admin/add_film.html", form=form, error=error)


@admin_bp.route("/admin/update-film/<int:film_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def update_films(film_id):
    my_film = MyFilms.get_by_id(film_id)
    if my_film is None:
        abort(404)
    #form = FilmForm(obj=my_film)
    f_opening = str(my_film.film_opening).split('-')
    date_opening = datetime.date(int(f_opening[0]), int(f_opening[1]), int(f_opening[2]))
    form = FilmForm(
        title=my_film.film_title, category=my_film.film_category,
        premiere=date_opening, synopsis=my_film.film_synopsis,
        film_image=werkzeug.datastructures.FileStorage(my_film.film_image))

    if form.validate_on_submit():
        my_film.film_title = form.title.data
        my_film.film_category = form.category.data
        my_film.film_opening = form.premiere.data
        my_film.film_synopsis = form.synopsis.data
        new_image = form.film_image.data
        image_name = None
        if new_image is not None:
            print(f'la imagen es esta: {new_image}, tipo de dato{type(new_image)}')
            image_name = secure_filename(new_image.filename)
            images_dir = current_app.config['FILMS_IMAGES_DIR']
            os.makedirs(images_dir, exist_ok=True)
            file_path = os.path.join(images_dir, image_name)
            new_image.save(file_path)
            my_film.film_image = image_name
        my_film.save()
        return redirect(url_for('admin.index'))
    return render_template("admin/add_film.html", form=form)


@admin_bp.route("/admin/delete-film/<int:film_id>/", methods=['POST', 'GET'])
@login_required
@admin_required
def delete_films(film_id):
    my_film = MyFilms.get_by_id(film_id)
    if my_film is None:
        abort(404)
    my_film.delete()
    return redirect(url_for('admin.index'))



#--------------------------------------------------------------#
#------------------------  PROYECTIONS  -----------------------#
@admin_bp.route("/admin/create/proyection", methods=['GET', 'POST'])
@login_required
@admin_required
def add_proyection():
    form = ProyectionsForm()
    error = None
    if form.validate_on_submit():
        #MyFilms.query.filter_by(title=form.title.data)
        film_id = MyFilms.get_by_filmname(form.film_name.data)
        film_name = form.film_name.data
        room_name = form.room_name.data
        proyection_time = form.proyection_time.data
        proyection_date = form.proyection_date.data
        myproyection = Proyections.verify_Date(proyection_date)
        m_proyection = Proyections.verify_Proyection(film_name, proyection_date, proyection_time)
        my_proyection = Proyections.verify_opening(film_id, proyection_date)
        if myproyection is not True or m_proyection is not None or my_proyection is False:
            if myproyection is not True:
                error = f'La fecha {proyection_date} ha de ser superior a 2 dias'
            elif my_proyection is False:
                error = f'La fecha de proyeccción ha de ser superior a la fecha de estreno'
            elif m_proyection is not None:
                error = f'La pelicula {film_name} ya tiene una proyeccion en este tiempo {proyection_time}, {proyection_date} '
        else:
            myproyection = Proyections(
                film_id=film_id.id, film_title=film_name, room_number=room_name, 
                proyection_time=proyection_time, proyection_date=proyection_date)
            myproyection.save()
            return redirect(url_for('admin.index'))
    return render_template("admin/add_proy.html", form=form, error=error)


@admin_bp.route("/admin/create/room", methods=['GET', 'POST'])
@login_required
@admin_required
def add_room():
    form = RoomsForm()
    error = None
    if form.validate_on_submit():
        room_name = form.room_name.data
        seatss_number = form.seatss_number.data
        myroom = MyRooms.get_by_roomname(room_name)
        if myroom is not None:
            error = f'El nombre {room_name} ya está en uso'
        else:
            myroom = MyRooms(rooms_name=room_name, seatss_number=seatss_number)
            myroom.save()
            return redirect(url_for('admin.index'))
    return render_template("admin/add_room.html", form=form, error=error)









