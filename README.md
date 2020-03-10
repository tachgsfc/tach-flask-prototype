# TACH Flask Prototype

This is a prototype of TACH in [Flask](https://flask.palletsprojects.com/).

The stack consists of the following tools:
- Python environment management with [Poetry](https://python-poetry.org)
- Data model in [SQLAlchemy](https://www.sqlalchemy.org)
- REST API with [safrs](https://github.com/thomaxxl/safrs)

## Setting up your environment

1.  Make sure that you are using Pyton 3.7 or later:

        $ python --version
        Python 3.8.2

2.  Install Poetry:

        $ pip install poetry

3.  Check out this repository:

        $ git clone http://github.com/tachgsfc/tach-flask-prototype
        $ cd tach-flask-prototype

4.  Install this project and all dependencies in a Python virtual environment:

        $ poetry install

## Start the server

1.  Run the following command to drop into the Python virtual environment:

        $ poetry shell

2.  Initialize the database:

        $ tach createdb

3.  Start the web server:

        $ tach run

4.  Open a web browser and navigate to http://localhost:5000.
