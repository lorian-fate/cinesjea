from flask_wtf import FlaskForm
from wtforms import (
    StringField, SubmitField,
    IntegerField
)
from wtforms.validators import DataRequired, Length





class TicketForm(FlaskForm):
    seatss_number = IntegerField("seats's number")
    submit = SubmitField('submit')