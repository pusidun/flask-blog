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
