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
		for prop in record.values[0]:
			node[prop] = record.values[0][prop]
		dataset['response'].append(node)
	return jsonify(dataset)


def query_cases_by_role(role, name, surname):
	name = name[0].upper() + name[1:].lower()
	surname = surname[0].lower() + surname[1:].lower()

	query_str = 'MATCH (case) WHERE case.' + role + ' =~ "' + name + '.*" AND case.' + role + ' =~ ".*' + surname + '.*" RETURN case'
	result = query_db(query_str)
	if len(result) == 0:
		query_str = 'MATCH (case) WHERE case.' + role + ' =~ "' + name + '.*" OR case.' + role + ' =~ ".*' + surname + '.*" RETURN case'
		result = query_db(query_str)
	return result


def is_string(str):
    return type(str).__name__ == 'str'


def advanced_cases_query(d_surname, d_name, p_surname, p_name, d_org = '', p_org = '',
						 date = '', keywords = '', reference = '', appeals = 0):
	query_str = 'MATCH (case)'

	if appeals == '1':
		query_str += '-[:`HAS_APPEAL`]->(appeal)'

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

	return query_db(query_str)