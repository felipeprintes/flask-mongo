#!/usr/bin/env python
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)
mongo = PyMongo(app)

app.config['MONGO2_DBNAME'] = 'flask-pymongo'
app.config['MONGO2_URI'] = 'mongodb://preety:f123456@ds217351.mlab.com:17351/flask-pymongo'
app.config['MONGO2_PORT'] = 27017

mongo = PyMongo(app, config_prefix='MONGO2')

@app.route('/')
def index():
	if 'username' in session:
		return 'você está logado, ' + session['username']

	return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
	users = mongo.db.users
	login_user = users.find_one({'name' : request.form['username']})

	if login_user:
		if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
		#if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
			session['username'] = request.form['username']
			return redirect(url_for('index'))

	return 'usuário ou senha inválida'


@app.route('/register', methods=['POST', 'GET'])
def register():
	if request.method=='POST':
		users = mongo.db.users
		existing_user = users.find_one({'name' : request.form['username']})		

		if existing_user is None:
			hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
			users.insert({'name' : request.form['username'], 'password' : hashpass})
			session['username'] = request.form['username']
			return redirect(url_for('index'))

		return 'Esse usuário ja existe'

	return render_template('register.html')


if __name__=='__main__':
	app.secret_key='meusegredo'
	app.run(debug=True, port=app.config['MONGO2_PORT'])



	
	
