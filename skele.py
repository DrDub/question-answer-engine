#!/usr/bin/python


### Imports ###
import nltk
from nltk.corpus import brown
import re
import sys
import os
import table_answer
import pickle
###############

if(len(sys.argv) != 3):
	print "Please call skele.py as follows: python skele.py <article.txt> <question.txt>!"
	exit(1)
	
	
### Globals ###
regexp_tagger = nltk.RegexpTagger(
	[(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
	(r'(The|the|A|a|An|an)$', 'AT'),   # articles
	(r'.*able$', 'JJ'),                # adjectives
	(r'.*ness$', 'NN'),                # nouns formed from adjectives
	(r'.*ly$', 'RB'),                  # adverbs
	(r'.*s$', 'NNS'),                  # plural nouns
	(r'.*ing$', 'VBG'),                # gerunds
	(r'.*ed$', 'VBD'),                 # past tense verbs
	(r'.*', 'NN')                      # nouns (default)
])



unigram_tagger = pickle.load(open("unigram_tagger.bin", "r"))
bigram_tagger = pickle.load(open("bigram_tagger.bin", "r"))
trigram_tagger = pickle.load(open("trigram_tagger.bin", "r"))
	
	
###############
def main():
	
	question = open(sys.argv[2], "r").readline()
	article = open(sys.argv[1], "r")
	
	# Now parse it and then get parts of speech
	sentTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	sentenceList = sentTokenizer.tokenize(article.read())
	print "DEBUG: " + str(sentenceList)
	### The PunktStringTokenizer is nice, will find sentences, we'll need this later
	wordTokenizer = nltk.PunktWordTokenizer()
	### Get a list of words again (will separate punctuation and whatnot)
	listOfWords = wordTokenizer.tokenize(question)
	
	### Create tagger and get POS ###
	
	result = trigram_tagger.tag(listOfWords)
	
	### Answer Stuff ###
	### Regexp Answer ###
	#regexp_answer.regexp_answer(question, result, open(sys.argv[1], "r"))
	#table_answer.run(listOfWords, result, )
	
	# Print results
	#print result
	

### If running as a console script ###
if (__name__ == "__main__"):
	main()