from os import path
from flask import Blueprint

auth = Blueprint(
    'auth', 
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'auth'),
    url_prefix='/auth',
)

from . import views