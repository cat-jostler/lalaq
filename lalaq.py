# TODO: rebuild from scratch, with feeling

import traceback
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


# each table is defined as a class
# db.create_all() does nothing (if the schema has not changed?)
# __tablename__ defaults to the class's name, so it doesn't hurt to specify it

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(31))
    password = db.Column(db.String(31))

    # Evidently you don't have to define these, but we did anyway.

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)


from datetime import datetime


class Posts(db.Model):
    __tablename__ = 'posts'

    author = db.Column


# TODO: implement something to do with Alembic at some point

if __name__ == '__main__':
    # baby's first try-catch-except
    # isn't that cute?
    try:
        app.run()

    except Exception as e:
        print(e)

# TODO: remind user to commit changes before terminating app
