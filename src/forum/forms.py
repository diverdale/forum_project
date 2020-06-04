from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired, DataRequired, Email, EqualTo
from wtforms import ValidationError
from src.models import User, Category


class NewTopicForm(FlaskForm):
    choices = Category.query.all()
    print(f'Choices= {choices}')
    topic_title = StringField('Title', validators=[DataRequired()])
    topic_category = SelectField('Category', choices=[(choice.id, choice.category_name)
                                                      for choice in choices])
    topic_content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')
