import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from blog import create_app
from blog import models
from blog.config import DevConfig, ProducCFG
#import fake_data


# create app 
app = create_app(DevConfig)
# Init manager obj
manager = Manager(app)

# Init migrate obj
migrate = Migrate(app, models.db)

# Create a new command server
# This cmd will run development_env Flask server
manager.add_command('server', Server(host='0.0.0.0', port=5000))
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    '''
        Create a python CLI.

        return: Default import object
        type: `Dict`
    '''
    return dict(app = app,
                db = models.db,
                User = models.User,
                Post = models.Post,
                Comment = models.Comment,
                Tag = models.Tag,)


if __name__ == '__main__':
    manager.run()
