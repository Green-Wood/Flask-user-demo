from os import getenv


class BaseConfig:
    SECRET_KEY = getenv('SECRET_KEY', 'greenwood')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTPLUS_MASK_SWAGGER = False

    PGUSER = getenv('PGUSER', 'greenwood')
    PGPASSWORD = getenv('PGPASSWORD', '')
    PGDATABASE = getenv('PGDATABASE', 'flask-user-demo')
    PGPORT = getenv('PGPORT', '5432')
    PGHOST = getenv('PGHOST', 'localhost')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'. \
        format(user=PGUSER, pw=PGPASSWORD, host=PGHOST, port=PGPORT, db=PGDATABASE)


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True


class ProductConfig(BaseConfig):
    pass


config = {
    'dev': DevelopmentConfig,
    'test': TestConfig,
    'prod': ProductConfig
}
