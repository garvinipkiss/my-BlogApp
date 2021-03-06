
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE



login_manager = LoginManager()
login_manager.session_protection ='strong'
login_manager.login_view = 'auth.login'

simple = SimpleMDE()
mail = Mail()
#initializing flask extension
bootstrap =Bootstrap()
db =SQLAlchemy()


def create_app(config_name):

  app=Flask(__name__)

  #creating the app configurations
  app.config.from_object(config_options[config_name])
  db.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)
  simple.init_app(app)

  #initializing bootstrap
  bootstrap.init_app(app)


  #we will add the views and the forms
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)



  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

  from .admin import admin as admin_blueprint
  app.register_blueprint(admin_blueprint,url_prefix = '/admin')



  return app
