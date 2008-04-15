#!/usr/bin/python
#
# Todo...make it so that this is a window based scheme and not based on sentence
# if the window is the best return the sentence that it came from
# we move through the sentence by incremementally moving our window to the right
# one word at a time
#
#

import nltk
import re
import sys
import os
import math

tokenizer 		= nltk.tokenize.punkt.PunktWordTokenizer()
sent_tokenizer 	= nltk.tokenize.punkt.PunktSentenceTokenizer()
stemmer 		= nltk.PorterStemmer()
sim_list 		= []

#-------------------------------------------------------------------------------
# main()
#
# Start Point
#
#-------------------------------------------------------------------------------
def main(strQuestion, articleFile):

	csim_answer(strQuestion, articleFile)

#-------------------------------------------------------------------------------
# Cosine Similarity Answer
#
# This function will allow you to give it an article and a question and it will
# return the sentence from the file that is most likely to answer the given 
# question.
#
#-------------------------------------------------------------------------------
def csim_answer(question, articleFile):
	
	# Generate the question vector
	q_stems = get_stems(question)
	q_vector = get_vector(q_stems)
	
	# Get the sentences from the file
	article			 = articleFile.read()
	article_sents 	 = sent_tokenizer.tokenize(article)

	# Sentence with the most likely answer
	maxSim = 0
	maxAns = ""
	
	# Go through each sentence in the article and generate a vector for it
	# We can then use this vector to compare it against the question vector
	# and we will store this value in our sim_list
	for sent in article_sents:
		#print sent
		
		vector = get_vector(get_stems(sent))
		
		cs = calc_sim(q_vector, vector)

		if cs > maxSim:
			maxSim = cs
			maxAns = sent
		
		#print "\n"
	print maxAns
	
	
#-------------------------------------------------------------------------------
# get_stems(sent)
# 
# This function will return an array of words which are the stemmed
# words from the sentence. 
#
#-------------------------------------------------------------------------------
def get_stems(sent):
	sent_parts = tokenizer.tokenize(sent)
	stems = []
	
	for part in sent_parts:
		stems.append(stemmer.stem(part))
		
	return(stems)

#-------------------------------------------------------------------------------
# get_vector(stem_list)
# 
# This function will return a nltk.defaultdict() which contains our vector
# representation of a given sentence given its stem_list
#
#-------------------------------------------------------------------------------
def get_vector(stem_list):

	vector = nltk.defaultdict(int)
	
	for stem in stem_list:
		vector[stem] += 1
	
	return vector
	
#-------------------------------------------------------------------------------
# calc_sim(q_vector, s_vector)
# 
# This function will use cosine similarity to compute the similarity of two 
# sentences.
#
#-------------------------------------------------------------------------------
def calc_sim(q_vector, s_vector):
	
	sim 	= 0
	num 	= 0
	qden	= 0
	sden	= 0
	
	for word in s_vector.keys():
		num 	+= s_vector[word] * q_vector[word]
		qden 	+= q_vector[word] ** 2
		sden	+= s_vector[word] ** 2
	
	if qden*sden==0:
		return 0
		
	sim		= (num) / ( math.sqrt(qden) * math.sqrt(sden) )
	
	return sim

		
		
		
		
		
		
		
### If running as a console script ###
if (__name__ == "__main__"):
	main()	
	
