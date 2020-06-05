from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, DataRequired, Email, EqualTo
from wtforms import ValidationError
from src.models import User, Roll


class LoginForm(FlaskForm):
    user_email = StringField('Email', validators=[DataRequired(), Email()])
    user_password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    user_email = StringField('Email', validators=[DataRequired(), Email()])
    user_username = StringField('Username', validators=[DataRequired()])
    user_password = PasswordField('Password', validators=[DataRequired(),
                                                          EqualTo('pass_confirm', message='Passwords mismatch')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        print(field)
        if User.query.filter_by(user_email=field).first():
            return True

    def check_username(self, field):
        if User.query.filter_by(user_username=field).first():
            return True


class EditUserForm(FlaskForm):
    choices = Roll.query.all()

    user_email = StringField('Email', validators=[DataRequired(), Email()])
    user_username = StringField('Username', validators=[DataRequired()])
    user_role = SelectField('Role', choices=[(choice.roll_name, choice.roll_name)
                                                         for choice in choices], default=2)
    user_password = PasswordField('Password', validators=[DataRequired(),
                                                          EqualTo('pass_confirm', message='Passwords mismatch')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
