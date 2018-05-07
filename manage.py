from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
import main
import models


#Init manager obj
manager = Manager(main.app)

#Init migrate obj
migrate = Migrate(main.app, models.db)

# Create a new command server
# This cmd will run development_env Flask server
manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    '''
        Create a python CLI.

        return: Default import object
        type: `Dict`
    '''
    return dict(app = main.app,
                db = models.db,
                User = models.User,
                Post = models.Post,
                Comment = models.Comment,
                Tag = models.Tag,)


if __name__ == '__main__':
    manager.run()
