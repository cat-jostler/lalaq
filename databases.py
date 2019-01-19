# Database wrangling???

from config import Config


class Database(object):
    def __init__(self):
        for database, uri in Config.SQLALCHEMY_BINDS:
            # setattr(object, name, value) = object.name = value
            setattr(self, database, __import__(database))
            # you really need to understand what that last parameter does
            # because you sure don't right now
            # go brush up on getters and setters and all that OO jazz

# this seems redundant, probably because you're mashing two peoples' code
# snippets together. shameful
# see if you can figure out how this differs from create_engine(database)
# in session.py
