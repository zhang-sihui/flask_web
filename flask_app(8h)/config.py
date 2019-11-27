import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'  # 1

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 10
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'  # 7
    FLASKY_MAIL_SENDER = 'Flasky Admin <1195796096@qq.com>'  # 8
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_ADMIN = '1195796096@qq.com'  # 9

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.qq.com')  # 2
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))  # 3
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'true').lower() in \
        ['true', 'on', '1']  # 4
    MAIL_USERNAME = '1195796096@qq.com'  # 5
    MAIL_PASSWORD = 'cstmclqhuitqifjc'  # 6

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_RUL') or \
                              'sqlite://'


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
    # 'default': ProductionConfig
}
