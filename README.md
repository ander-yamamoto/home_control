# home_control

Python API for simple home control

Simple light bulb remote control using Tasmota SONOFF miniR2 and a Beaglebone Black as MQTT broker.
This Python API is a MQTT client, monitoring changes of status of the light bulbs.
The Light status is stored to a slqite db.
The API will serve web and mobile clients


Python modules:
Flask (tryed to install fastapi on BBB but failed)
SQLite3
Paho MQTT
