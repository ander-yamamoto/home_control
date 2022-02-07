import datetime
from sqlalchemy import update
from flask import Blueprint

from .models import Node
from .. import app 
from .. import db
from .. import mqtt




@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('tele/+/STATE')

    with app.app_context():
        node = Node.query.filter_by(category="lamp")
        for row in node:
            mqtt.subscribe('stat/'+row.topic+'/'+row.item_id)
        for row in node:
            mqtt.publish('cmnd/'+row.topic+'/'+row.item_id, None)


@mqtt.on_topic('stat/#')
def handle_switch(client, userdata, message):
    with app.app_context():
        #print('Received message on topic {}: {}'.format(message.topic, message.payload.decode()))
        db.session.query(Node).\
            filter(Node.topic == message.topic.split('/')[1], Node.item_id == message.topic.split('/')[2]).\
            update({'status':(message.payload == b'ON'),'last_update':datetime.datetime.now() }, synchronize_session="fetch")
        db.session.commit()
        #print (Node.query.filter_by(topic=message.topic.split('/')[1], item_id=message.topic.split('/')[2])[0].status)


@mqtt.on_topic('tele/+/STATE')
def handle_state(client, userdata, message):
    with app.app_context():
        #print('Received message on topic {}: {}'.format(message.topic, message.payload.decode()))
        db.session.query(Node).\
            filter(Node.topic == message.topic.split('/')[1]).\
            update({'last_update' : datetime.datetime.now() }, synchronize_session="fetch")
        db.session.commit()
        #for row in Node.query.filter_by(topic=message.topic.split('/')[1]):
        #    print (row.last_update)

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print("msg: "+message.topic)
