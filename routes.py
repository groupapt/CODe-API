__author__ = 'Desira Daniel'

from flask import Flask, render_template, request
from utils import query_db, form_json, query_cases_by_role, advanced_cases_query, query_str_start, query_str_end

app = Flask(__name__)
app.debug = True

DEF_ROUTE = '/api/0.1/'
JSON_ROUTE = DEF_ROUTE + 'json/'


@app.route(JSON_ROUTE + 'case/<int:reference_p1>/<int:reference_p2>')
def case(reference_p1, reference_p2):
	reference_p1 = str(reference_p1)
	reference_p2 = str(reference_p2)
	query_str = query_str_start() + 'WHERE case.reference = "' + reference_p1 + '/' + reference_p2 + '"' + query_str_end() + ' LIMIT 1'
	result = query_db(query_str)
	return form_json(result)


@app.route(JSON_ROUTE + 'appeal/<int:reference_p1>/<int:reference_p2>/<int:reference_p3>')
def appeal(reference_p1, reference_p2, reference_p3):
	reference_p1 = str(reference_p1)
	reference_p2 = str(reference_p2)
	reference_p3 = str(reference_p3)
	query_str = query_str_start(True) + 'WHERE appeal.reference = "' + reference_p1 + '/' + reference_p2 + '/' + reference_p3 + '"' + query_str_end(True) + ' LIMIT 1'
	result = query_db(query_str)
	return form_json(result)


@app.route(JSON_ROUTE + 'cases/date/<date>')
def date_cases(date):
	query_str = query_str_start() + 'WHERE case.date = "' + date + '"' + query_str_end()
	result = query_db(query_str)
	return form_json(result)


@app.route(JSON_ROUTE + 'cases/year/<int:year>')
def year_cases(year):
	query_str = 'MATCH (date)-[:HAS_CASES]->(case) WHERE date.year = "' + str(year) + '" RETURN case'
	result = query_db(query_str)
	return form_json(result)


@app.route(JSON_ROUTE + 'cases/appeals')
def appeals():
	result = query_db(query_str_start(True) + query_str_end(True))
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


@app.route(JSON_ROUTE +'cases/prosecutor/<prosecutor_surname>/<prosecutor_name>')
def pros_cases(prosecutor_surname, prosecutor_name):
	return form_json(query_cases_by_role('prosecutor', prosecutor_name, prosecutor_surname))


@app.route(JSON_ROUTE + 'cases/judges/<judge_surname>/<judge_name>')
def judge_cases(judge_surname, judge_name):
	judge_surname = judge_surname.upper()
	judge_name = judge_name.upper()

	query_str = query_str_start() + 'WHERE judge.j_surname =~ "' + judge_surname + '.*" AND judge.j_name =~ "' + judge_name + '.*"' + query_str_end()
	result = query_db(query_str)
	if len(result) == 0:
		query_str = query_str_start() + 'WHERE judge.j_surname =~ "' + judge_surname + '.*" OR judge.j_name =~ "' + judge_name + '.*"' + query_str_end()
		result = query_db(query_str)
	return form_json(result)


@app.route(JSON_ROUTE + 'cases/keywords/<keywords>')
def keywords_cases(keywords):
	keywords = keywords.split(',')
	query_str = query_str_start() + 'WHERE '
	for keyword in keywords:
		query_str += '"' + keyword + '" IN case.keywords AND '
	query_str += '1 = 1' + query_str_end()
	return form_json(query_db(query_str))


@app.errorhandler(404)
def not_found(error):
	return render_template('notfound.json'), 404


@app.errorhandler(500)
def internal_error(error):
	return render_template('internalerror.json'), 500

if __name__ == '__main__':
	app.run()