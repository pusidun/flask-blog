from flask import url_for, redirect, render_template, flash, session, request
from . import auth
from .forms import LoginForm, RegisterForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''router for login'''

    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=form)
    else:
        if form.validate_on_submit():
            flash("Login in success!")
            return redirect(url_for('main.home'))
        else:
            return render_template('login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    '''router for register'''

    form = RegisterForm()

    if request.method == 'GET':
        return render_template('register.html', form=form)
    else:
        if form.validate_on_submit():
            flash('register success')
            return redirect(url_for('auth.login'))
        else:
            return render_template('register.html', form=form)