from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config
from flask_login import LoginManager

login_Manager=LoginManager()
login_Manager.session_protection='strong'
login_Manager.login_view='auth.login'

bootstrap=Bootstrap()
mail=Mail()
moment = Moment()
db=SQLAlchemy()


# factory function
def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')
    login_Manager.init_app(app)
    return app

