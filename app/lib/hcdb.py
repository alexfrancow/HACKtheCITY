import sqlite3
import subprocess
import os

def create_hackthecity_db(db):
	db = db.replace(" ", "_")
	os.system("mkdir volumes/"+db)
	db2 = [("volumes/"+db,)]
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
	db = db.replace(" ", "_")
	db = subprocess.getoutput("pwd")+"/db/"+db+".db"
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("SELECT volume FROM docker")
	path = c.fetchone()
	return path


def select_databases():
	dbs = os.listdir("db")
	return dbs
