from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField
from wtforms.validators import DataRequired, Length
from app.models import User


class CommentForm(FlaskForm):
    '''Form validator for comment.'''

    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    text = TextField(u'Comment', validators=[DataRequired()])
