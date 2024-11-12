from flask import render_template, redirect, url_for, request, current_app
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import login_manager
from . import auth_bp
from .forms import SignUpForm, LogInForm
from .models import User
from app.models import MyFilms, Proyections



@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('global_access.index'))
    form = SignUpForm()
    error = None
    if form.validate_on_submit():
        name = form.username.data
        email = form.email.data
        password = form.password.data
        user = User.get_by_username(name)
        if user is not None:
            error = f'El Usuario {name} ya está en uso'
        else:
            user = User(username=name, email=email)
            user.set_password(password)
            user.save()
            
            """login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('global_access.index')"""
            return redirect('auth.login')
    return render_template('auth/signup.html', form=form, error=error)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('global_access.index'))
    error = None
    form = LogInForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is None:
            error = f"este usuario no existe"
        elif user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                if current_user.is_admin:
                    next_page = url_for('admin.index') 
                else:
                    next_page = url_for('global_users.index')
            return redirect(next_page)
        else:
            error = f"nombre de usuario o contraseña incorrectos"
    return render_template('auth/login.html', form=form, error=error)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))
