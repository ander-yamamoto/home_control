Home Control


Use to control lamps at home.

-Some Sonoff mini r2
-beaglebone black running ubuntu18.04
-mosquitto mqtt broker


How to use it:
-clone repository then activate venv:
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip 
python3 -m pip install -r requirements.txt
```

-to activate in Windows use:
```
python3 -m venv .venv
.\\.venv\Scripts\activate
python3 -m pip install --upgrade pip 
python3 -mpip install -r requirements.txt
```

-and after done editing:
```
deactivate
```

-To init database type on a python terminal:
```
from project import db, create_app, models
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
```

-Sonoff devices should be added to database using sqlite3:
```
INSERT INTO node (name, topic, item_id, ip, status, category, last_update)
VALUES ("NAME TO SHOW", "TOPIC CONFIGURED IN SONOFF", "SONOFF ITEM, USUALLY POWER", "SONOFF IP", 0, "lamp", CURRENT_TIMESTAMP);
```


-To run flask server (visible at http://localhost:5000, local machine only):
```
export FLASK_APP=project
export FLASK_DEBUG=1
flask run
```




-To run flask server (visible by other machines on http://[Server IP]:5000 ):
```
export FLASK_APP=project
export FLASK_DEBUG=1
flask run --host=0.0.0.0
```



-To run waitress server (visible by other machines on http://[Server IP]:5000 ):
```
Linux:
./.venv/bin/waitress-serve --port=5000 --call 'project:create_app'

Windows:
.\.venv\Scripts\waitress-serve.exe --port=5000 --call 'project:create_app'
```

-to run as a service (BeagleboneBLack-Ubuntu):
```
sudo nano /etc/systemd/system/homecontrol.service

[Unit]
Description=home control app
After=network.target

[Service]
User=ubuntu
WorkingDirectory=[PATH TO CLONE]/flask_auth_app
ExecStart=flask_auth_app/.venv/bin/waitress-serve --call 'project:create_app'
Restart=always

[Install]
WantedBy=multi-user.target


sudo systemctl daemon-reload

```