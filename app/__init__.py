from flask import Flask, redirect, url_for, render_template
from .main.forms import CommentForm
from .models import db


def create_app(config):
    '''Create app'''
    
    app = Flask(__name__)

    db.init_app(app)

    # Get the config from obj of DevConfig
    app.config.from_object(config)

    @app.route('/')
    def main_page():
        return redirect(url_for('main.home'))

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html") ,404

    # Register the Blueprint into app object
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
