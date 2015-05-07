# Introduction #

How answer resolution will work from a high level down to the implementation.


# Details #

The problem we are facing is what to do when a question returns several candidate answers. How do we know which one to choose? Should we merge the answers into one question?

Suppose that the following question was asked...

  * "Where are apples produced?"

And the potential answers that are returned are...

  * China produced about two-fifths of this total.
  * United States is the second leading producer, with more than 7.5% of the world production.
  * Turkey, France, Italy and Iran are among the leading apple exporters.

Problems that we have
  * The question might have been where are apples grown? This has about the same meaning as produced but how do we know this?
  * The results might have said "China grows about two-fifths of this total".
  * We need to combine the results into one coherent answer in this example but how do we know what to return? For example we may want to return "China, United States" or maybe "China produced about two-fifths of this total and united states is the second leading producer

Solutions
  * We can use wordnet and search for variants on the question
  * We can simple list all of the possible answers.

# Question Scenarios #

One method for identifying the correct answer from the list is to break questions done for per question type perhaps. Have different scenarios for different types of questions.
  * Who
  * What
  * When
  * Where
  * Why
  * Default scenario

For example where could look for proper nouns and non proper noun places. So we can look through the results list and try to go through and identify a proper noun that might answer the question and if we don't find that then we look for words that wordnet associates with places and see if they answer the question.

So we could go through and try to use our established scenario methods for answering the question and if none of the work out then we can fall back onto a default scenario that can be used to generally answer a question.

**Who**

**What**

**When**

**Where**

**Why**

**Default**