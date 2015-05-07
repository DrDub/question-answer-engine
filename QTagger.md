# Introduction #

This document will describe the QTagger's architecture and then its implementation.


# Architecture #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages

# Implementation #

We will be using a tri-gram tagger with a bigram tagger backoff. The Bigram tagger will use a unigram tagger as its backoff, and if needed the unigram tagger will use a regular expression based tagger as its backoff.

We will be training these taggers with the complete brown corpus.

The problem with this is that creating and training the taggers takes a considerable amount of time even on a moderately fast computer so there is a utility called "...." that will allow you to generate a binary file representation of each tagger using the Python pickle library. These binary files can then be loaded later on and be used to greatly reduce the amount of time the system will require to startup.
