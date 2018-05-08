from flask import Flask, redirect, url_for
from .config import DevConfig
from .forms import CommentForm
from .models import db
from .controllers.blog import blog_blueprint


app = Flask(__name__)
db.init_app(app)

# import the views modules
# views = __import__('controllers')

# Get the config from obj of DevConfig
app.config.from_object(DevConfig)

@app.route('/')
def index():
    # Redirect the Request_url '/' to /blog
    return redirect(url_for('blog.home'))

# Register the Blueprint into app object
app.register_blueprint(blog_blueprint)

if __name__ == '__main__':
    app.run()