from flask_wtf import FlaskForm
from wtforms import (
    StringField, SubmitField,
    PasswordField, BooleanField,
    SelectField,  IntegerField
)
from wtforms.validators import (
    DataRequired, Email,
    Length
)


class SignUpForm(FlaskForm):
    username = StringField("Nombre", validators=[DataRequired(), Length(max=40)])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('Sign up')


class LogInForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Log in")


class TicketForm(FlaskForm):
    film_session = StringField()
    seatss_number = IntegerField("seats's number")
    submit = SubmitField('submit')
    