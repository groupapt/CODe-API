__author = 'Daniel'

from collections import defaultdict
from SOAPpy import SOAPProxy
from operator import itemgetter

'''
' Diagnoses a piece of text and gives back the top 5 keywords
' @param text Text to process
' @return List of the common 5 common nouns
'''


def generate_keywords(text):
	server = SOAPProxy('http://metanet4u.research.um.edu.mt/services/MtPOS?wsdl')

	# '_NN' is 3 characters long
	words = [w[:-3] for w in server.tagParagraphReturn(text).split(' ') if w[-2:] == 'NN']

	word_dict = defaultdict(int)
	for word in words:
		word_dict[word] += 1

    # returning the most common keywords
	return [x[0] for x in (sorted(word_dict.iteritems(), key=itemgetter(1), reverse=True)[:5])]