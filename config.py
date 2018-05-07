class Config(object):
    '''base config class.'''
    pass

class ProducCFG(Config):
    '''Production config class.'''
    pass

class DevConfig(Config):
    '''Development config class.'''
    # Open DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:****@127.0.0.1:3306/flask_blog'
