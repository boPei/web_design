from flask import Blueprint

main=Blueprint('main',__name__)
# from pythonProj.Flask.FlaskWebDevProj.app.main import views,errors
from . import views,errors
