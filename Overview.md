## Introduction ##

This article will describe at a very high level how the Question-Answer-Engine will work and provide information for obtaining more detailed information about the project.

## High Level Overview ##

![http://question-answer-engine.googlecode.com/files/QuestionAnswerEngineFlow.png](http://question-answer-engine.googlecode.com/files/QuestionAnswerEngineFlow.png)

  * Question is a string. It is fed to OpenNLP, which generates a QStruct.
  * The QStruct is then fed to the Answering Agent.
  * The Answering agent uses a statistical approach (more details)
  * The Answering agent is a big blob that collects answers
  * The answering agent can then produce an answer
  * More details go here