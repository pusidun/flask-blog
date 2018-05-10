import os
from flask import Blueprint


main = Blueprint(
    'main',
    __name__,
    template_folder=os.path.join(os.path.pardir, 'templates', 'main'),
    url_prefix='/main',
)

from . import views
