from flask import Flask, request  #, redirect, url_for, render_template, flash
from flask import jsonify
from models import *

app = Flask(__name__)
# app.config.from_object(__name__)

@app.teardown_request
def teardown_request(exception):
	db.close()  # close the db connection

'''
@app.route('/BR/', methods=['GET'])
def show0():
	resultSet_ = Branch.select()
	data = [i.serialize for i in resultSet_]
	response_ = jsonify( data )
	response_.status_code = 200
	return response_
'''
	
@app.route('/BR/<int:HeadOfficeID>/', methods=['GET'])
def show1(HeadOfficeID:int):
	resultSet_ = Branch.select().where(Branch.hqID == HeadOfficeID)
	response_ = jsonify( [i.serialize for i in resultSet_] )
	response_.status_code = 200 # success
	return response_


@app.route('/BR/<int:HeadOfficeID>/', methods=['POST'])
def add1(HeadOfficeID:int):
	'''
	curl -X POST -H "Content-Type: application/json" -d '{}' http://localhost:5000/BR/1/
	'''
	dataFromHttpRequest = request.get_json()
	c = Branch(id = dataFromHttpRequest['id'], name = dataFromHttpRequest['name'], hqID = HeadOfficeID)
	c.save(force_insert=True)
	# return jsonify({'message': 'OK'})
	return jsonify(message="No ids provided.",
                    category="error",
                    status=404


@app.route('/BR/@/<int:branchID>/', methods=['POST'])
def edit1(branchID:int):
	data = request.get_json()
	q = Branch.select().where(Branch.id == int(branchID)).get()
	q.name = data['name']
	q.hqID = data['code']
	q.save() # force_insert=True)
	'''
	q = Branch.update(name=dataFromHttpRequest['name'], hqID=dataFromHttpRequest['code']).where(Branch.id == branchID)
	q.execute()
	'''
	return jsonify({'update': 'OK'})


@app.route('/BR/-/<int:branchID>/', methods=['POST'])
def delete1(branchID:int):
	e = Branch.delete().where(Branch.id == int(branchID))  # .get()
	e.execute()
	return jsonify({'delete': 'OK'})

	
@app.route('/HQ/')
def show2():
	resultSet_ = Headquarter.select()
	data = [i.serialize for i in resultSet_]
	return jsonify( data ) # return json.dumps({'name': 'alice', 'email': 'alice@outlook.com'})

@app.errorhandler(404)
def not_found(error = None):
	message = {
		'status' : 404,
		'message' : 'Not found: ' + request.url,
	}
	resp = jsonify( message )
	resp.status_code = 404
	return resp
	
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000, debug = True)

'''
INSERT INTO headquarter VALUES (1, 'Cusco 01'); 
INSERT INTO branch VALUES(1, 'Sede Cusco 01', 1);

from datetime import date
uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save() # bob is now stored in the database
# Returns: 1
bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
grandma = Person.select().where(Person.name == 'Grandma L.').get()
# https://docs.peewee-orm.com/en/latest/peewee/quickstart.html#model-definition
https://docs.peewee-orm.com/en/latest/peewee/models.html#models-without-a-primary-key
https://docs.peewee-orm.com/en/latest/peewee/api.html#Model.replace
https://www.fullstackpython.com/flask-json-jsonify-examples.html

DEBUG = True
SECRET_KEY = 'hello_world'

@app.route('/')
def show_entries():
	data = BlogPost.select()
	return render_template('show_entries.html', data=data)

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
	if request.method == 'POST':
		entry = BlogPost(title = request.form['title'], text = request.form['description'])
		entry.save()
		flash('New entry was successfully posted')
		return redirect(url_for('show_entries'))
	return render_template('add.html')
'''