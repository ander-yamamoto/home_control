from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Node
from .. import mqtt
from . import main


@main.route('/')
def index():
    nodes = Node.query.filter_by(category='lamp')

    return render_template('index.html', nodes=nodes)

@main.route('/', methods=['POST'])
def index_post():
    nodes = Node.query.filter_by(category='lamp')
    if 'bt1' in request.form:
        for row in nodes:
            mqtt.publish('cmnd/'+ row.topic + '/' + row.item_id, 'ON')


    elif 'bt2' in request.form:
        for row in nodes:
            mqtt.publish('cmnd/'+ row.topic + '/' + row.item_id, 'OFF')

    else:
        for row in nodes:
            if row.name in request.form:
                if row.status == 0:
                    mqtt.publish('cmnd/'+ row.topic + '/' + row.item_id, 'ON')
                else:
                    mqtt.publish('cmnd/'+ row.topic + '/' + row.item_id, 'OFF')



    return redirect(url_for('main.index'))

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

