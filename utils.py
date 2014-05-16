__author__ = 'Desira Daniel'

from flask.json import jsonify
from py2neo import neo4j


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
	query_str = 'MATCH (case) WHERE case.' + role + ' =~ "' + name + '.*" AND case.' + role + ' =~ ".*' + surname + '.*" RETURN case'
	result = query_db(query_str)
	if result is None:
		query_str = 'MATCH (case) WHERE case.' + role + ' =~ "' + name + '.*" OR case.' + role + ' =~ ".*' + surname + '.*" RETURN case'
		result = query_db(query_str)
	return result