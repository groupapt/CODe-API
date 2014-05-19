__author__ = 'Desira Daniel'

from flask import Flask, render_template, request
from utils import query_db, form_json, query_cases_by_role, advanced_cases_query

app = Flask(__name__)
app.debug = True

DEF_ROUTE = '/api/0.1/'
JSON_ROUTE = DEF_ROUTE + 'json/'


@app.route(JSON_ROUTE + 'case/<reference_p1>/<reference_p2>')
def case(reference_p1, reference_p2):
	result = query_db('MATCH (case) WHERE case.reference = "' + reference_p1 + '/' + reference_p2 + '" RETURN case LIMIT 1')
	return form_json(result)


@app.route(JSON_ROUTE + 'cases/date/<date>')
def date_cases(date):
	result = query_db('MATCH (case) WHERE case.date = "' + date + '" RETURN case')
	return form_json(result)


@app.route(JSON_ROUTE + 'cases/year/<int:year>')
def year_cases(year):
	result = query_db('MATCH (date)-[:HAS_CASES]->(case) WHERE date.year = "' + str(year) + '" RETURN case')
	return form_json(result)


@app.route(JSON_ROUTE + 'cases/appeals')
def appeals():
	result = query_db('MATCH (case)-[:HAS_APPEAL]->(appeal) RETURN appeal')
	return form_json(result)


@app.route(JSON_ROUTE + 'cases')
def cases():
	args = request.args

	return form_json(advanced_cases_query(d_surname=args.get('d_surname'),
										  d_name=args.get('d_name'),
										  p_surname=args.get('p_surname'),
										  p_name=args.get('p_name'),
										  d_org=args.get('d_org'),
										  p_org=args.get('p_org'),
										  date=args.get('date'),
										  keywords=args.get('keywords'),
										  reference=args.get('reference'),
										  appeals=args.get('appeals')))


@app.route(JSON_ROUTE + 'cases/defendant/<defendant_surname>/<defendant_name>')
def def_cases(defendant_surname, defendant_name):
	return form_json(query_cases_by_role('defendant', defendant_name, defendant_surname))


@app.route(JSON_ROUTE +'/cases/prosecutor/<prosecutor_surname>/<prosecutor_name>')
def pros_cases(prosecutor_surname, prosecutor_name):
	return form_json(query_cases_by_role('prosecutor', prosecutor_name, prosecutor_surname))


@app.route(JSON_ROUTE + '/cases/judges/<judge_surname>/<judge_name>')
def judge_cases(judge_surname, judge_name):
	judge_surname = judge_surname.upper()
	judge_name = judge_name.upper()

	query_str = 'MATCH (judge)-[]->(case) WHERE judge.j_surname =~ "' + judge_surname + '.*" AND judge.j_name =~ "' + judge_name + '.*" RETURN case, judge'
	result = query_db(query_str)
	if len(result) == 0:
		query_str = 'MATCH (judge)-[]->(case) WHERE judge.j_surname =~ "' + judge_surname + '.*" OR judge.j_name =~ "' + judge_name + '.*" RETURN case'
		result = query_db(query_str)
	return form_json(result)


@app.route(JSON_ROUTE + '/cases/keywords/<keywords>')
def keywords_cases(keywords):
	keywords = keywords.split(',')
	query_str = 'MATCH (case) WHERE '
	for keyword in keywords:
		query_str += '"' + keyword + '" IN case.keywords AND '
	query_str += '1 = 1 RETURN case'
	return form_json(query_db(query_str))


@app.errorhandler(404)
def not_found(error):
	return render_template('notfound.json'), 404


@app.errorhandler(500)
def internal_error(error):
	return render_template('internalerror.json'), 500

if __name__ == '__main__':
	app.run()