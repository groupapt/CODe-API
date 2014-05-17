__author__ = 'Desira Daniel'

from flask import Flask, render_template, request
from utils import query_db, form_json, query_cases_by_role, advanced_cases_query

app = Flask(__name__)
app.debug = True


@app.route('/case/<reference_p1>/<reference_p2>')
def case(reference_p1, reference_p2):
	result = query_db('MATCH (case) WHERE case.reference = "' + reference_p1 + '/' + reference_p2 + '" RETURN case LIMIT 1')
	return form_json(result)


@app.route('/cases/date/<date>')
def date_cases(date):
	result = query_db('MATCH (case) WHERE case.date = "' + date + '" RETURN case')
	return form_json(result)


@app.route('/cases/year/<int:year>')
def year_cases(year):
	result = query_db('MATCH (date)-[:HAS_CASES]->(case) WHERE date.year = "' + str(year) + '" RETURN case')
	return form_json(result)


@app.route('/cases/query')
def cases():
	args = request.args

	if args.get('d_surname') and args.get('d_name'):
		d_surname = args.get('d_surname')
		d_name = args.get('d_name')
	else:
		d_surname = ''
		d_name = ''

	if args.get('p_surname') and args.get('p_name'):
		p_surname = args.get('p_surname')
		p_name = args.get('p_name')
	else:
		p_surname = ''
		p_name = ''

	if args.get('d_org'):
		d_org = args.get('d_org')
	else:
		d_org = ''

	if args.get('p_org'):
		p_org = args.get('p_org')
	else:
		p_org = ''

	if args.get('date'):
		date = args.get('date')
	else:
		date = ''

	return form_json(advanced_cases_query(d_surname, d_name, p_surname, p_name, d_org, p_org, date))


@app.route('/cases/defendant/<defendant_surname>/<defendant_name>')
def def_cases(defendant_surname, defendant_name):
	return form_json(query_cases_by_role('defendant', defendant_name, defendant_surname))


@app.route('/cases/prosecutor/<prosecutor_surname>/<prosecutor_name>')
def pros_cases(prosecutor_surname, prosecutor_name):
	return form_json(query_cases_by_role('prosecutor', prosecutor_name, prosecutor_surname))


@app.route('/cases/judges/<judge_surname>/<judge_name>')
def judge_cases(judge_surname, judge_name):
	judge_surname = judge_surname.upper()
	judge_name = judge_name.upper()

	query_str = 'MATCH (judge)-[:JUDGES]->(case) WHERE judge.j_surname =~ "' + judge_surname + '.*" AND judge.j_name =~ "' + judge_name + '.*" RETURN case'
	result = query_db(query_str)
	if len(result) == 0:
		query_str = 'MATCH (judge)-[:JUDGES]->(case) WHERE judge.j_surname =~ "' + judge_surname + '.*" OR judge.j_name =~ "' + judge_name + '.*" RETURN case'
		result = query_db(query_str)
	return form_json(result)


@app.route('/cases/keywords/<keywords>')
def keywords_cases(keywords):
	keywords = keywords.split(',')


@app.errorhandler(404)
def not_found(error):
	return render_template('notfound.json'), 404


@app.errorhandler(500)
def internal_error(error):
	return render_template('internalerror.json'), 500

if __name__ == '__main__':
	app.run()