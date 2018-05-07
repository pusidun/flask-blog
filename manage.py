from flask_script import Manager, Server
import main


manager = Manager(main.app)

# Create a new command server
# This cmd will run development_env Flask server
manager.add_command('server', Server())

@manager.shell
def make_shell_context():
    '''
        Create a python CLI.

        return: Default import object
        type: `Dict`
    '''
    return dict(app = main.app)


if __name__ == '__main__':
    manager.run()
