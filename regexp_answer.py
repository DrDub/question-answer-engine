#!/usr/bin/python


### Imports ###
import nltk
import re
import sys
import os
###############

def regexp_answer(listQuestion):
	"""Takes a question list tagged and tokenized and attempts to return a true/false value for easy questions."""
	
	### First, rebuild the question in string form to use as a regex ###
	for group in listQuestion:
		print group