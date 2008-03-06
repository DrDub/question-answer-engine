#!/usr/bin/python


### Imports ###
import nltk
import re
import sys
import os
###############

if(len(sys.argv) < 2):
	print "Please pass a string as command line arguments!"
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

	
	
	
###############
def main():
	# Join the arguments to form a string
	# Later, we'll take something that isn't a command line string
	string = list(sys.argv[1:])
	string = " ".join(string)
	print "Your string is: %s" % string
	
	# Now parse it and then get parts of speech
	#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	### The PunktStringTokenizer is nice, will find sentences, we'll need this later
	tokenizer = nltk.PunktWordTokenizer()
	### Get a list of words again (will separate punctuation and whatnot)
	listOfWords = tokenizer.tokenize(string)
	
	### Get POS
	result = regexp_tagger.tag(listOfWords)
	
	# Print results
	print result
	

### If running as a console script ###
if (__name__ == "__main__"):
	main()