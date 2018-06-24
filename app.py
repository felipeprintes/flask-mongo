#!/usr/bin/env python
from flask import Flask
from flask_pymongo import PyMongo
from flask import render_template

app = Flask(__name__)
mongo = PyMongo(app)

app.config['MONGO2_DBNAME'] = 'flask-pymongo'
app.config['MONGO2_URI'] = 'mongodb://preety:f123456@ds217351.mlab.com:17351/flask-pymongo'
app.config['MONGO2_PORT'] = 27017

mongo = PyMongo(app, config_prefix='MONGO2')

@app.route('/')
def add():
	user = mongo.db.users
	user.insert({'name':'Fulano'})
	user.insert({'name':'Marcio'})
	user.insert({'name':'Anderson'})
	user.insert({'name':'Bruno'})
	user.insert({'name':'Ciclano'})
	user.insert({'name':'Carlos'})
	user.insert({'name':'Vitor'})
	user.insert({'name':'Beltrano'})
	return 'Usuário adicionado'


if __name__=='__main__':
	app.run(debug=True, port=app.config['MONGO2_PORT'])



	
	
