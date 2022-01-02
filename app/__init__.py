from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from logging.handlers import SMTPHandler
from flask_mail import Mail
import logging


login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings_module)

    app.config.from_pyfile('config.py', silent=True)
    #configure_logging(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    db.init_app(app)
    migrate.init_app(app, db)

    #Registro de blueprints
    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .global_access import global_access_bp
    app.register_blueprint(global_access_bp)
    
    from .global_users import global_users_bp
    app.register_blueprint(global_users_bp)

    return app
    
"""
user:ADMIN/1234
user:ettamae/etta
"""

