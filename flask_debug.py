# This might not even be necessary.

from flask.cli import main

if __name__ == '__main__':
    main(as_module=False)
    # remember, False is a default value for as_module
