from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import json
import click



app = Flask(__name__)
app.config.from_file('config.json', load=json.load)
db = SQLAlchemy(app)
login_manager = LoginManager(app)



 
from TODO import routes

@click.command(name='create_user')
def create_user():
    import create_user


app.cli.add_command(create_user)

  