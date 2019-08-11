from flask import Blueprint, render_template
from flask import Flask, jsonify, Blueprint, render_template, request, flash, redirect, url_for, flash, Response
import time
import json

main_blueprint = Blueprint('main', __name__, template_folder='templates')
app = Flask(__name__)

@main_blueprint.route('/', methods= ['GET', 'POST'])
def main():
    return render_template('index.html')

@main_blueprint.route('/setup', methods=['POST'])
def setup():
    def message():
            json_data = print("hola")
            time.sleep(1)
            return json_data

    if request.method == 'POST':
        city = request.form['city']
        print(city)
        if request.method == 'radio1':
            zabbix_scripts = request.form['']
        if request.method == ' radio2':
            openvas_ip = request.form['']
        if request.method == 'radio3':
            openvas_ips = request.form['']
        if request.method == 'radio4':
            print(1)
    return Response(message(), mimetype='text/html')
    #return Response(message(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug= True)
