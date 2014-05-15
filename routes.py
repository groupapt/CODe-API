__author__ = 'Desira Daniel'

from flask import Flask, render_template
from flask.json import jsonify
from py2neo import neo4j

app = Flask(__name__)
app.debug = True


def query_db(statement):
	graph_db = neo4j.GraphDatabaseService()
	result = neo4j.CypherQuery(graph_db, statement).execute()
	dataset = {'response': []}
	for r in result:
	    node = {}
	    for property in r.values[0]:
		    node[property] = r.values[0][property]
	    dataset['response'].append(node)
	return jsonify(dataset)

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

@app.route('/cases/prosecutor/<prosecutor_surname>/<prosecutor_name>')
def pros_cases(prosecutor_surname, prosecutor_name):

	return query_db('MATCH (case) WHERE case.prosecutor =~ \'' + prosecutor_name + '.*\' RETURN case')

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
	return render_template('notfound.json'), 404

if __name__ == '__main__':
	app.run()