from uuid import uuid4
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

from app.models import User, db


class LoginForm(FlaskForm):
    '''Login form'''

    username = StringField('Username', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('Password', validators=[DataRequired()])

    def validate_on_submit(self):
        check_validate = super().validate_on_submit()

        if not check_validate:
            return False
        
        # check username is exist
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            flash("This username has been registered.")
            self.username.errors.append('Invalid username or password')
            return False

        # check the password
        if not user.verify_password(self.password.data):
            flash("Please check your password.")
            self.username.errors.append('Invalid username or password')
            return False
    
        return True


class RegisterForm(FlaskForm):
    '''Register Form.'''

    username = StringField('Username', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])

    def validate_on_submit(self):
        check_validate = super().validate_on_submit()

        # if not validate
        if not check_validate:
            return False

        # Check user whether exists
        user = User.query.filter_by(username=self.username.data).first()
        print(self.username.data)
        if user:
            self.username.errors.append('User already exists.')
            return False
        print('before db')
        # add valid new_user to database
        new_user = User(id=str(uuid4()), username=self.username.data, password=self.password.data)
        db.session.add(new_user)
        db.session.commit()

        return True
