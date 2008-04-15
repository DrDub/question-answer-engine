### Imports ###
import nltk
from nltk.corpus import treebank
import re
import sys
import os
import regexp_answer
import pickle
###############

def main():
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

    training_data = treebank.tagged_sents()
           
    unigram_tagger = nltk.UnigramTagger(training_data, backoff=regexp_tagger)
    bigram_tagger = nltk.BigramTagger(training_data, backoff=unigram_tagger)
    trigram_tagger = nltk.TrigramTagger(training_data, backoff=bigram_tagger)

    unigram_pickler = pickle.Pickler(open("unigram_tagger.bin","w"))
    bigram_pickler = pickle.Pickler(open("bigram_tagger.bin","w"))
    trigram_pickler = pickle.Pickler(open("trigram_tagger.bin","w"))

    unigram_pickler.dump(unigram_tagger)
    bigram_pickler.dump(bigram_tagger)
    trigram_pickler.dump(trigram_tagger)

### If running as a console script ###
if (__name__ == "__main__"):
       main()
