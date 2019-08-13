import sqlite3
import subprocess

def create_hackthecity_db(db):
	db2 = [(db,)]
	db = subprocess.getoutput("pwd")+"/db/"+db+".db"
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute('''CREATE TABLE nmap
		(ip text, ports text, web text, location real, city real)''')
	c.execute('''CREATE TABLE docker
	     	(volume text)''')
	c.executemany("INSERT INTO docker VALUES (?);", (db2))

	conn.commit()
	conn.close()


def check_volume_path(db):
	db = subprocess.getoutput("pwd")+"/db/"+db+".db"
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("SELECT volume FROM docker")
	path = c.fetchone()
	return path

