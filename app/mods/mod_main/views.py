from flask import Blueprint, render_template
from flask import Flask, jsonify, Blueprint, render_template, request, flash, redirect, url_for, flash, Response
from app.lib.hcdb import create_hackthecity_db, check_volume_path, select_databases
from app.lib.maxmind import hosts_up
import time
import json
import os
import subprocess
import socket

main_blueprint = Blueprint('main', __name__, template_folder='templates')
app = Flask(__name__)

@main_blueprint.route('/', methods= ['GET', 'POST'])
def main():

    # Comprueba si hay alguna BD
    db_exists = len(os.listdir("db"))
    if db_exists == 0:
        return render_template('index.html')

    else:
        return redirect('/choose_db')


@main_blueprint.route('/choose_db', methods= ['GET', 'POST'])
def choose_db():
    dbs = select_databases()
    return render_template('choose_db.html', dbs=dbs)


@main_blueprint.route('/use_db', methods= ['GET', 'POST'])
def use_db():
    db = request.form['city']
    db = db.replace(".db", "")
    volume = check_volume_path(db)
    volume = ''.join(volume)
    volume = subprocess.getoutput("pwd")+"/"+volume
    os.system("cp compose.yml docker-compose.ymll")
    fin = open("docker-compose.ymll", "rt")
    fout = open("docker-compose.yml", "wt")
    for line in fin:
        fout.write(line.replace('$VOLUME', volume))
    fin.close()
    fout.close()
    os.system("rm docker-compose.ymll")
    os.system("sysctl -w vm.max_map_count=262144")
    os.system("chmod -R 777 volumes")
    print(db)
    ips = hosts_up(db)
    print(ips)

    os.system("docker-compose up")
    time.sleep(30)

    return render_template('dashboard.html', db=db)

@main_blueprint.route('/create_db', methods= ['GET', 'POST'])
def create_db():
    return render_template('index.html')


@main_blueprint.route('/setup', methods=['POST'])
def setup():
    time.sleep(20)
    if request.method == 'POST':
        city = request.form['city']
        create_hackthecity_db(city)

    return redirect("/")

if __name__ == '__main__':
    app.run(debug= True)
