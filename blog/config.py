class Config(object):
    '''base config class.'''
    SECRET_KEY = "442263c62e4062925486acb003653c90"

class ProducCFG(Config):
    '''Production config class.'''
    pass

class DevConfig(Config):
    '''Development config class.'''
    # Open DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1994@1227@127.0.0.1:3306/flask_blog'
