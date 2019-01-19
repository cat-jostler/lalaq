# Create a unique engine and session for each database.
# Allows access to all databases at once.
# Keep everything in its own session.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

engines = []
sessions = []

for database, uri in Config.SQLALCHEMY_BINDS:
    engine = create_engine(uri)
    engines.append(engine)
    sessions.append(sessionmaker(bind=engine))

# cargo-culted code, sorry

# take a look at the binds={} parameter - seems the difference is the above
# code does exactly what it says on the tin, while calling sessionmaker with
# binds opens a single session shared by all engines
# if binds is used, what's the implication for "result objects" - will they
# end up somewhere they shouldn't because they're now all bound to the same
# session regardless of the database/engine they're associated with?
