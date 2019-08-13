from flask import Blueprint, render_template
from flask import Flask, jsonify, Blueprint, render_template, request, flash, redirect, url_for, flash, Response
from app.lib.hcdb import create_hackthecity_db, check_volume_path
import time
import json
import os

main_blueprint = Blueprint('main', __name__, template_folder='templates')
app = Flask(__name__)

@main_blueprint.route('/', methods= ['GET', 'POST'])
def main():
    db_exists = len(os.listdir("db"))
    if db_exists == 0:
        return render_template('index.html')
    else:
        return Response(db_exists, mimetype='text/html')


@main_blueprint.route('/setup', methods=['POST'])
def setup():
    time.sleep(30)
    if request.method == 'POST':
        city = request.form['city']
        print(city)
        create_hackthecity_db(city)

        if request.method == 'radio1':
            zabbix_scripts = request.form['']
        if request.method == ' radio2':
            openvas_ip = request.form['']
        if request.method == 'radio3':
            openvas_ips = request.form['']
        if request.method == 'radio4':
            print(1)

    return Response("hola", mimetype='text/html')
    #return Response(message(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug= True)
