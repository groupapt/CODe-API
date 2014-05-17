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


def advanced_cases_query(d_surname, d_name, p_surname, p_name, d_org = '', p_org = '', date = ''):
	query_str = ''
	if d_org != '':
		query_str = 'MATCH (case) WHERE LOWER(case.defendant) =~ ".*' + d_org.lower() + '.*"'
	elif d_name != '' or d_surname != '':
		query_str = 'MATCH (case) WHERE case.defendant =~ "' + d_name + '.*" AND case.defendant =~ ".*' + d_surname + '.*"'

	if p_org != '':
		if query_str == '':
			query_str = 'MATCH (case) LOWER(case.defendant) =~ ".*' + d_org.lower() + '.*"'
		else:
			query_str += ' AND LOWER(case.defendant) =~ ".*' + d_org.lower() + '.*"'
	elif p_name != '' or d_surname != '':
		if query_str == '':
			query_str = 'MATCH (case) WHERE case.prosecutor =~ "' + p_name + '.*" AND case.prosecutor =~ ".*' + p_surname + '.*"'
		else:
			query_str += ' AND case.prosecutor =~ "' + p_name + '.*" AND case.prosecutor =~ ".*' + p_surname + '.*"'

	if date != '':
		query_str += ' AND case.date = "' + date + '"'

	query_str += ' RETURN case'
	print query_str
	return query_db(query_str)