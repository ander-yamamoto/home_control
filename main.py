#external import
from dotenv import dotenv_values
from multiprocessing import Process

#local .py files
import database_node
import database_user
import mqtt


def test_db_node():


	db_node_create(('luz_sala', 'luz_sala', '´power1', '192.168.0.32', 0, datetime.datetime.now()))
	(node, er) = db_node_read(('luz_sala',))
	print (node)
	if er:
	        print (er)


def main():
	config = dotenv_values(".env")
	db_node_init()
	db_user_init()



	p_mqtt = Process(target=mqtt.mqtt_init, args=(config,))
	p_mqtt.start()
	p_test = Process(target=test_db_node, )
	p_test = start()	
	p_mqtt.join()



if __name__ == '__main__':
    main()
