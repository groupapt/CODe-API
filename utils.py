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
	query_str = 'MATCH (case) WHERE case.' + role + ' =~ "' + name + '.*" AND case.' + role + ' =~ ".*' + surname + '.*" RETURN case'
	result = query_db(query_str)
	if len(result) == 0:
		query_str = 'MATCH (case) WHERE case.' + role + ' =~ "' + name + '.*" OR case.' + role + ' =~ ".*' + surname + '.*" RETURN case'
		result = query_db(query_str)
	return result