from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Node



main = Blueprint('main', __name__)

@main.route('/')
def index():
    nodes = Node.query.all()
    return render_template('index.html', nodes)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

