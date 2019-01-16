from lalaq import app, db, User


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)

# This no longer appears to be necessary either.
