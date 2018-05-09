from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField
from wtforms.validators import DataRequired, Length
from blog.models import User


class CommentForm(FlaskForm):
    '''Form validator for comment.'''

    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    text = TextField(u'Comment', validators=[DataRequired()])


class LoginForm(FlaskForm):
    '''Login form'''

    username = StringField('Username', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('Password', validators=[DataRequired()])

    def validate(self):
        check_validate = super(LoginForm, self).validate_on_submit()

        if not check_validate:
            return False

        # check username is exist
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        # check the password
        if not user.verify_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False
    
        return True
