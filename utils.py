__author__ = 'Desira Daniel'

from flask.json import jsonify
from py2neo import neo4j


def query_db(query_str):
	graph_db = neo4j.GraphDatabaseService()
	return neo4j.CypherQuery(graph_db, query_str).execute()


def form_json(result):
	dataset = {'response': []}
	for record in result:
		node = {}
		for value in record.values:
			for prop in value:
				node[prop] = value[prop]
		dataset['response'].append(node)
	return jsonify(dataset)


def query_cases_by_party(name, surname):
	name = name[0].upper() + name[1:].lower()
	surname = surname[0].lower() + surname[1:].lower()

	query_str = query_str_start() + 'WHERE case.defendant =~ "' + name + '.*" AND case.defendant =~ ".*' + surname + '.*" OR case.prosecutor =~ "' + name + '.*" AND case.defendant =~ ".*' + surname + '.*"' + query_str_end()
	result = query_db(query_str)
	if len(result) == 0:
		query_str = query_str_start() + 'WHERE case.defendant =~ "' + name + '.*" OR case.defendant =~ ".*' + surname + '.*" OR case.prosecutor =~ "' + name + '.*" OR case.defendant =~ ".*' + surname + '.*"' + query_str_end()
		result = query_db(query_str)
	return result


def is_string(str):
	return type(str).__name__ == 'str'


def query_str_start(appeal_check = False):
	query_str = 'MATCH (judge)-[]->(case)'
	if appeal_check:
		query_str += '-[]->(appeal)'
	query_str += '-[]->(court) '
	return query_str


def query_str_end(appeal_check = False):
	query_str = ' RETURN judge, court, case'
	if appeal_check:
		query_str += ', appeal'
	return query_str


def advanced_cases_query(d_surname, d_name, p_surname, p_name, d_org = '', p_org = '',
						 date = '', keywords = '', reference = '', appeals = 0):
	query_str = 'MATCH (judge)-[]->(case)'

	if appeals == '1':
		query_str += '-[]->(appeal)'

	query_str += '-[]->(court)'

	if is_string(d_org):
		query_str += ' WHERE LOWER(case.defendant) =~ ".*' + d_org.lower() + '.*"'
	elif is_string(d_name) or is_string(d_surname):
		query_str += ' WHERE case.defendant =~ "' + d_name + '.*" AND case.defendant =~ ".*' + d_surname + '.*"'

	if is_string(p_org):
		if query_str == 'MATCH (case)':
			query_str += ' WHERE LOWER(case.defendant) =~ ".*' + d_org.lower() + '.*"'
		else:
			query_str += ' AND LOWER(case.defendant) =~ ".*' + d_org.lower() + '.*"'
	elif is_string(p_name) or is_string(d_surname):
		if query_str == '':
			query_str = 'MATCH (case) WHERE case.prosecutor =~ "' + p_name + '.*" AND case.prosecutor =~ ".*' + p_surname + '.*"'
		else:
			query_str += ' AND case.prosecutor =~ "' + p_name + '.*" AND case.prosecutor =~ ".*' + p_surname + '.*"'

	if is_string(date):

		query_str += ' AND case.date = "' + date + '"'

	if appeals == '1':
		query_str += ' RETURN appeal'
	else:
		query_str += ' RETURN case'

	query_str += ', judge, court'

	return query_db(query_str)