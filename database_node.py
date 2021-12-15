import sqlite3
import datetime

database = 'data.db'

def init():
	conn = sqlite3.connect(database)
	cursor = conn.cursor()

	cursor.execute("""
	CREATE TABLE IF NOT EXISTS node (
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL UNIQUE,
			topic TEXT NOT NULL,
			item_id TEXT NOT NULL,
			ip VARCHAR(16) NOT NULL,
			status INTEGER NOT NULL,
			last_update timestamp NOT NULL
	);
	""")

	print('NODE db init successful')
	conn.close()



def create (node):
	conn = sqlite3.connect(database)
	cursor = conn.cursor()

	try:
		cursor.execute("""
		INSERT INTO node (name,	topic, item_id,ip, status, last_update)
		VALUES (?,?,?,?,?,?)""", node)

	except sqlite3.Error as er:
		print ("ERROR: ".join(er.args))
	else:
		conn.commit()
		print ('NODE inserted')
	finally:
		conn.close()


def read(col, condition, param):
	er = None
	conn = sqlite3.connect(database)
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT "+col+" FROM node WHERE "+condition + " ?", param)
	
	except sqlite3.Error as er:
		print ('Error reading from DB '.join(er.args))
	else:
		data = cursor.fetchall()
	finally:
		conn.close()
		return (data, er)


def updatetime (client, userdata, msg):
	conn = sqlite3.connect(database)
	cursor = conn.cursor()
	try:
		cursor.execute("""UPDATE node SET last_update=? WHERE topic=?""", (datetime.datetime.now(),msg.topic.split('/')[1],))

	except sqlite3.Error as er:
		print ('Error updating timestamp '.join(er.args))
	else:
		conn.commit()
		print ('Timestamp updated')
	finally:
		conn.close()


def updatestate (client,userdata,msg):
	conn = sqlite3.connect(database)
	cursor = conn.cursor()

	try:
		
		state = (msg.payload == b'ON')
		cursor.execute("""UPDATE node SET status=? WHERE topic=? AND item_id=?""",(state ,msg.topic.split('/')[1],msg.topic.split('/')[2],))

	except sqlite3.Error as er:
		print ('Error updating status '.join(er.args))
	else:
		conn.commit()
		print ('status updated')
	finally:
		conn.close()
	
