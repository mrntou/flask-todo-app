from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired
from datetime import datetime

# ------------------------------------------------------------------------------



class LoginForm(FlaskForm):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign in')


class TodoForm(FlaskForm):
	title = StringField(validators=[DataRequired()])
	submit = SubmitField('Add Task')