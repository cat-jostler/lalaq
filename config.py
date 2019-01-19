class Config(object):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    # SQLAlchemy URI format: database+driver://user:password@ip:port/db_name
    # TODO: make the following ~more dynamic~
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://user:pass@server:port/"
    # nts these are databases, not tables
    # you can make all the tables in the world elsewhere, but not here
    SQLALCHEMY_BINDS = {
        'users': SQLALCHEMY_DATABASE_URI + 'users',
        'posts': SQLALCHEMY_DATABASE_URI + 'posts',
        'materials': SQLALCHEMY_DATABASE_URI + 'materials'
    }
    # you can find an obnoxious way to populate SQLALCHEMY_BINDS later
