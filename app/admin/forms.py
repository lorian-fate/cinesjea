from flask_wtf import FlaskForm
from wtforms import (
    StringField, SubmitField, TextAreaField, BooleanField, 
    SelectField, IntegerField, DateField, TimeField
    )
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed
from app.models import MyFilms, MyRooms

from datetime import datetime


class FilmForm(FlaskForm):
    title = StringField('Títle', validators=[DataRequired(), Length(max=128)])
    category = SelectField('Choose an option', choices=[
        'Accion', 'Animacion', 'Aventuras', 'Belicas',
        'Ciencia Ficcion', 'Comedia', 'Crimen', 'Deportivas',
        'Drama', 'Fantasia', 'Futuristas', 'Historicas',
        'Musical', 'Policiacas', 'Religiosas', 'Suspense', 
        'Terror', 'Western'
    ])
    premiere = DateField('premiere', format='%Y-%m-%d', validators=[DataRequired()])
    synopsis = TextAreaField('Synopsis')
    film_image = FileField('Head Image', validators=[DataRequired(),
        FileAllowed(['jpg', 'png'], 'Allowed only')
    ])
    submit = SubmitField('submit')


class UserAdminForm(FlaskForm):
    is_admin = BooleanField('Administrator')
    submit = SubmitField('save')

class RoomsForm(FlaskForm):
    room_name = SelectField('Choose an option', choices=[
        'alfa', 'beta', 'gamma', 'delta',
        'epsilon', 'zeta', 'eta', 'theta',
        'iota', 'kappa', 'Lambda', 'mu',
        'nu', 'xi', 'omicron', 'pi', 
        'rho', 'sigma', 'tau', 'upsilon', 
        'phi', 'chi', 'psi', 'omega'
    ])
    seatss_number = IntegerField("seats's number")
    submit = SubmitField('submit')

class ProyectionsForm(FlaskForm):
    film_name = SelectField()
    room_name = SelectField()
    proyection_time = TimeField('Proyection time', format='%H:%M', validators=[DataRequired()])
    proyection_date = DateField('Proyection Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('submit')

    def __init__(self):
        super(ProyectionsForm, self).__init__()
        self.film_name.choices = [(c.film_title) for c in MyFilms.get_all()]
        self.room_name.choices = [(c.id) for c in MyRooms.get_all()]

