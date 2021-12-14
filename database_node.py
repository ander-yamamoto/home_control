import sqlite3
import datetime

database = 'data.db'

def db_node_init():
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



def db_node_create (node):
	conn = sqlite3.connect(database)
	cursor = conn.cursor()

	try:
		cursor.execute("""
		INSERT INTO node (name,	topic, item_id,ip, status, last_update)
		VALUES (?,?,?,?,?,?)""", node)
	
	except sqlite3.Error as er:
		print ('Failed to create node '.join(er.args))
	else:
		conn.commit()
		print ('NODE inserted')
	finally:
		conn.close()
    

def db_node_read(param):
	er = None
	conn = sqlite3.connect(database)
	cursor = conn.cursor()
	try:
		cursor.execute("""
		SELECT * FROM node WHERE name=?""", param)
	
	except sqlite3.Error as er:
		print ('Error reading from DB '.join(er.args))
	else:
		node = cursor.fetchall()
	finally:
		conn.close()
		return (node, er)


