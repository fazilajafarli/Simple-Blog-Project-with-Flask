from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return 'Login'



@auth.route('/signup')
def sign_up():
    return 'Sign up'


@auth.route('/logout')
def log_out():
    return 'Logout'