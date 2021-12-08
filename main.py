from dotenv import dotenv_values
import database
import mqtt



def main():
	config = dotenv_values(".env")
	database = "database.db"
	
	mqtt.mqtt_init(config)
	print (config)


if __name__ == '__main__':
    main()
