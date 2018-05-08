from flask import Flask
from config import DevConfig
import forms


app = Flask(__name__)

# import the views modules
views = __import__('views')

# Get the config from obj of DevConfig
app.config.from_object(DevConfig)

if __name__ == '__main__':
    app.run()