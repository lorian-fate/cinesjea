from flask import abort, render_template, current_app, request
from flask_login import current_user
from . import global_access_bp
from app.models import MyFilms, Proyections



@global_access_bp.route("/")
def index():
    myproyection = Proyections.get_next_ten_days()
    proyection_for_week = Proyections.get_by_week()
    proyection_for_month = Proyections.get_by_month()
    next_opening = MyFilms.get_nex_opening()
    all_pro = Proyections.get_all()
    return render_template(
                "global_access/index.html", 
                myproyection=myproyection, 
                next_opening=next_opening,
                this_week=proyection_for_week,
                this_month=proyection_for_month,
                all_P = all_pro)


@global_access_bp.route("/next-ten-days/<int:nextTD_id>")
def proyection_details_next(nextTD_id):
    my_proyection = Proyections.get_by_id(nextTD_id)
    all_proyFilm = Proyections.get_next_ten_days_from_film(my_proyection.film_id)
    return render_template("global_access/proy_ten.html", my_proy=my_proyection, all_ProyFilmTenDays=all_proyFilm)


@global_access_bp.route("/all/<int:myFilm_id>")
def proyection_details_all(myFilm_id):
    my_film = MyFilms.get_by_id(myFilm_id)
    allproy = Proyections.get_all_pro(myFilm_id)
    return render_template("global_access/proy_details.html", my_film=my_film, all_Proy=allproy)



@global_access_bp.route("/month/<int:myFilm_id>")
def proyection_details_month(myFilm_id):
    my_proyection = Proyections.get_proyections_by_film_id(myFilm_id)[0]
    month_proyFilm = Proyections.get_by_month_from_film(myFilm_id)
    return render_template("global_access/proy_month.html", my_proy=my_proyection, month_ProyFilm=month_proyFilm)


@global_access_bp.route("/week/<int:proyection_id>")
def proyection_details_week(proyection_id):
    my_proyection = Proyections.get_by_id(proyection_id)
    all_proyFilm = Proyections.get_by_week_from_film(my_proyection.film_id)
    return render_template("global_access/proy_week.html", my_proy=my_proyection, all_ProyFilm=all_proyFilm)


@global_access_bp.route("/seek/")
def busqueda():
    my_films = MyFilms.get_all()
    return render_template("global_access/seeker.html", all_films=my_films)





