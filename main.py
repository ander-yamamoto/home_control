#external import
from dotenv import dotenv_values
from multiprocessing import Process
import datetime

#local .py files
import database_node as node_db
import database_user as user_db
import mqtt

def main():
	config = dotenv_values(".env")
	node_db.init()
	user_db.init()



	p_mqtt = Process(target=mqtt.mqtt_init, args=(config,))
	p_mqtt.start()
	p_mqtt.join()



if __name__ == '__main__':
    main()
