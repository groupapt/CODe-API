__author__ = 'Desira Daniel'

from flask import Flask
from flask import render_template
from flask.json import dumps
from py2neo import cypher

app = Flask(__name__)
app.debug = True


def query_db(statement):
	session = cypher.Session('http://localhost:7474')
	transaction = session.create_transaction()

	transaction.append(statement)
	result = transaction.execute()
	transaction.commit()
	#print(dumps(result))

	return result

@app.route('/')
def index():
	return ''

@app.route('/case/<reference>')
def case(reference):
	return query_db('MATCH (case) WHERE case.reference = \'' + reference + '\' RETURN case')

@app.route('/cases/year/<int:year>')
def year_cases(year):
	return 'year'

@app.route('/case/<defendant>/<prosecutor>')
def def_pros_case(defendant, prosecutor):
	pass

@app.route('/cases/defendant/<defendant>')
def def_cases(defendant):
	return query_db('MATCH (case) WHERE case.defendant =~ \'' + defendant + '.*\' RETURN case')

@app.route('/cases/prosecutor/<prosecutor>')
def pros_cases(prosecutor):
	return query_db('MATCH (case) WHERE case.prosecutor =~ \'Godf.*\' RETURN case')
	#return query_db('MATCH (case) WHERE case.prosecutor =~ \'' + prosecutor + '.*\' RETURN case')

@app.route('/cases/town/<town>')
def town_cases(town):
	return ''

@app.route('/cases/judges/<judge_name>')
def judge_name_cases(judge_name):
	pass

@app.route('/cases/judges/<judge_surname>')
def judge_surname_cases(judge_surname):
	pass

@app.errorhandler(404)
def not_found(error):
	return render_template('error.json'), 404

if __name__ == '__main__':
	app.run()