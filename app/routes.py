from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@main.route('/profile')
def profile():
    return render_template('profile.html')
@main.route('/settings')