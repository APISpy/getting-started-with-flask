import json
from datetime import datetime

from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def home_view():
    return 'Welcome to our Library!'


@app.route('/template')
def template_view():
    return render_template('index.html', name='RMOTR')


@app.route('/parametrized/<string:name>/<int:age>',
           defaults={'target_year': 2020})
@app.route('/parametrized/<string:name>/<int:age>/<int:target_year>')
def parametrized_view(name, age, target_year):
    this_year = datetime.now().year
    difference = target_year - this_year
    future_age = age + difference

    params = {
        'name': name,
        'target_year': target_year,
        'this_year': this_year,
        'future_age': future_age
    }
    return render_template('age.html', **params)


@app.route('/json')
def json_view():
    request_info = {
        'IP': request.remote_addr,
        'path': request.path,
        'method': request.method,
        'headers': {k: v for k, v in request.headers}
    }
    return json.dumps(request_info), 200, {'Content-Type': 'application/json'}
