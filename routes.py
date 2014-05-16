__author__ = 'Desira Daniel'

from flask import Flask, render_template
from flask.json import jsonify
from py2neo import neo4j

app = Flask(__name__)
app.debug = True


def query_db(query_string):
	graph_db = neo4j.GraphDatabaseService()
	return neo4j.CypherQuery(graph_db, query_string).execute()

def form_json(result):
	dataset = {'response': []}
	for record in result:
		node = {}
		for property in record.values[0]:
			node[property] = record.values[0][property]
		dataset['response'].append(node)
	return jsonify(dataset)

def query_cases_by_role(role, name, surname):
	query_string = 'MATCH (case) WHERE case.' + role + ' =~ \'' + name + '.*\' AND case.' + role + ' =~ \'.*' + surname + '.*\' RETURN case'
	result = query_db(query_string)
	if result == None:
		query_string = 'MATCH (case) WHERE case.' + role + ' =~ \'' + name + '.*\' OR case.' + role + ' =~ \'.*' + surname + '.*\' RETURN case'
		result = query_db(query_string)
	return result

@app.route('/case/<reference_p1>/<reference_p2>')
def case(reference_p1, reference_p2):
	result = query_db('MATCH (case) WHERE case.reference = \'' + reference_p1 + '/' + reference_p2 + '\' RETURN case LIMIT 1')
	return form_json(result)

@app.route('/cases/year/<int:year>')
def year_cases(year):
	result = query_db('MATCH (date) WHERE date.year = ' + str(year) + ' RETURN date')
	return form_json(result)

@app.route('/case/<defendant>/<prosecutor>')
def def_pros_case(defendant, prosecutor):
	pass

@app.route('/cases/defendant/<defendant_surname>/<defendant_name>')
def def_cases(defendant_surname, defendant_name):
	return form_json(query_cases_by_role('defendant', defendant_name, defendant_surname))

@app.route('/cases/prosecutor/<prosecutor_surname>/<prosecutor_name>')
def pros_cases(prosecutor_surname, prosecutor_name):
	return form_json(query_cases_by_role('prosecutor', prosecutor_name, prosecutor_surname))

@app.route('/cases/town/<town>')
def town_cases(town):
	return ''

@app.route('/cases/judges/<judge_surname>/<judge_name>')
def judge_name_cases(judge_surname, judge_name):
	pass

@app.errorhandler(404)
def not_found(error):
	return render_template('notfound.json'), 404

@app.errorhandler(500)
def internal_error(error):
	return render_template('internalerror.json'), 500

if __name__ == '__main__':
	app.run()