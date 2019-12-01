from flask import Flask,render_template,session,redirect,url_for,request

import os

app = Flask(__name__)
#generating secret key
key = os.urandom(24) #random number
key = str(key)
#secret_key generated
app.secret_key = key
#index page
@app.route('/')
def index():
	if 'username' in session:
		username = session['username']
		return render_template('profile.html',name = username)
	return redirect(url_for('login'))
#login session
@app.route('/login',methods = ['GET','POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['name']
		return redirect(url_for('index'))
	return render_template('login.html')
#logout session
@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug = True)