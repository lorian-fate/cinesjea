from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user

from . import global_users_bp
from app.models import MyFilms, Proyections, MyTicket
from .forms import TicketForm

@global_users_bp.route("/users")
@login_required
def index():
    myproyection = Proyections.get_all()
    my_ticket = MyTicket.get_by_user_id(current_user.id)
    return render_template("global_users/index.html", next_pro=myproyection, my_ticket=my_ticket)


@global_users_bp.route('/get_ticket/<int:film_id>', methods=['GET', 'POST'])
@login_required
def get_ticket(film_id):
    my_film = MyFilms.get_by_id(film_id)
    allproy = Proyections.get_all_pro(film_id)
    form = TicketForm()
    error = None
    error1 = None
    if request.method == "POST":
        seatss_number = form.seatss_number.data
        my_id_pro = request.form.get('mysession')
        
        if seatss_number == None:
            error = f"cantidad de asientos no permitida"
        elif seatss_number < 1 or seatss_number >= 50:
            error = f"cantidad de asientos no permitida"
        elif my_id_pro == None:
            error1 = f"Debe elegir una opción"
        else:
            my_proyection = Proyections.get_by_id(my_id_pro)
            film_name = my_proyection.film_title
            room_number = my_proyection.room_number
            proyection_time = my_proyection.proyection_time
            proyection_date = my_proyection.proyection_date
            v_ticket = MyTicket.verifyTicket(film_name, room_number, proyection_time, proyection_date, seatss_number)
            if v_ticket != None:
                error = f"This place is ocupated"
            else:
                my_ticket = MyTicket(user_id=current_user.id, film_name=film_name, 
                                    room_number=room_number, proyection_time=proyection_time, 
                                    proyection_date=proyection_date, seatss_number=seatss_number)
                my_ticket.save()
                return redirect(url_for('global_users.index'))
    return render_template(
        'global_users/add_ticket.html', 
        form=form, my_film=my_film, 
        all_Proy=allproy, error=error, error1=error1)


@global_users_bp.route("/next-proyections/<int:myFilm_id>")
@login_required
def next_proyection(myFilm_id):
    my_film = MyFilms.get_by_id(myFilm_id)
    allproy = Proyections.get_all_pro(myFilm_id)
    return render_template("global_users/next_proy.html", my_film=my_film, all_Proy=allproy)
