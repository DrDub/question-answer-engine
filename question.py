#!/usr/bin/python
# -*- coding: cp1252 -*-


### Imports ###
import nltk
import re
import sys
import os
import pickle
###############

if(len(sys.argv) != 1):
	print "Please call question.py as follows: python question.py <article.txt>!"
	exit(1)
	
### Globals ###
regexp_tagger = nltk.RegexpTagger(
	[(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),     # cardinal numbers
	(r'([Tt]h(e)|(at))|([Aa]n?)$', 'DT'), # articles
	(r'.*able$', 'JJ'),                   # adjectives
	(r'.*ness$', 'NN'),                   # nouns formed from adjectives
	(r'.*ly$', 'RB'),                     # adverbs
	(r'.*s$', 'NNS'),                     # plural nouns
	(r'.*ing$', 'VBG'),                   # gerunds
	(r'.*ed$', 'VBD'),                    # past tense verbs
	(r'.*', 'NN'),                        # nouns (default)
])

unigram_tagger = pickle.load(open("unigram_tagger.bin", "r"))
bigram_tagger = pickle.load(open("bigram_tagger.bin", "r"))
trigram_tagger = pickle.load(open("trigram_tagger.bin", "r"))

stokenizer = nltk.PunktSentenceTokenizer()
wtokenizer = nltk.PunktWordTokenizer()

###############
def question():
	"""Tags and tokenizes a file and attempts to return a list of easy questions."""

	articleFile = "article.txt.sample" #sys.argv[1]

	### Read the article ###
	article = open(articleFile, "r").read()
	sentences = stokenizer.tokenize(article)
	words = [wtokenizer.tokenize(sentence) for sentence in sentences]
	stags = [trigram_tagger.tag(word) for word in words]

	r1 = re.compile("([^; ]*) DT;([^ ]*) NN;([^ ]*) VBD;([^ ]*) IN;([^ ]*) NNP")

	for stag in stags:
                s = ";".join([" ".join(st) for st in stag])
                m = r1.findall(s)
                if len(m)>0:
                        print ' '.join(['Did',m[0][0],m[0][1],m[0][2][0:-1],m[0][3],m[0][4]])+'?'
                

	#cfgFile = "grammar.rules"
	#cfg = open(cfgFile, "r").read()
	#grammarstags = []
	#for stag in stags:
	#	for tag in stag:
	#		grammarstags += [tag]
	#grammarstags = list(set(grammarstags))
	#for (word, tag) in grammarstags:
	#	cfg += tag + ' -> "' + word + '"\n'
	#print cfg
	#nltk.cfg._PARSE_CFG_RE = re.compile(
        #        r'''^\s*([\w,]+(?:[-/]\w+)?)\s*(?:[-=]+>)\s*(?:("[^"]+"|'[^']+'|[,\w-]+(?:/[\w-]+)?|\|)\s*)*$'''
        #        ,re.VERBOSE)
	#nltk.cfg._SPLIT_CFG_RE = re.compile(r'''([\w,]+(?:[/-]\w+)?|[-=]+>|"[^"]+"|'[^']+'|\|)''') 
	#rd_parser = nltk.RecursiveDescentParser(nltk.parse_cfg(cfg))
	#print words[0]
        #print rd_parser.nbest_parse(words[0])
	
	
	### Print the length of the article in words (just as a sanity check here) ###
	#print "DEBUG: " + str(len(article)) + " characters; " + str(len(stags)) + " sentences; " +
	
	### Search the article for our regex ###
	#answer = re.findall(regex, article, re.IGNORECASE)
	
	#if(answer[0].lower() == regex.lower()):
	#       print "Yes"
	#else:
	#       print "No"


### If running as a console script ###
if (__name__ == "__main__"):
	question()
