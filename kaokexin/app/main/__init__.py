from flask import Blueprint
main = Blueprint('main',__name__,template_folder='../',static_folder='static')
from . import views, errors