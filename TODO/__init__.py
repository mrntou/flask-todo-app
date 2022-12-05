from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import json

app = Flask(__name__)
app.config.from_file('config.json', load=json.load)
db = SQLAlchemy(app)
login_manager = LoginManager()



from TODO import routes