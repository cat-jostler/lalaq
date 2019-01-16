class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True  # did nothing, so setting FLASK_ENV manually here
    # SQLAlchemy URI format: database+driver://user:password@ip:port/db_name
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://user:password@ip:port/db_name"
    SQLALCHEMY_ECHO = True
