Lab Name 	: Computational Liguistics
Experiment Name : Fine - grained POS Tagging

How to run :
	To run the server, open the port on localhost using the run.py file. Domain is http://127.0.0.1:5000 . 
	On opening it in browser, you'll be first navigated to Introduction page.	

How to navigate :
	There are different pages (Introduction, Theory, Objective, Experiment, Quizzes, Procedure, Further Readings).
	You can navigate to any page using the links given in all webpages on the left.

Information on different pages
	Introduction :
		This page gives you an introduction to Parts Of Speech.

	Theory :
		This page will provide more knowledge about the Part Of Speech, it's types and more information about it.

	Objective :
		This page tells you the objective of this experiment.

	Experiment :
		This page is the actual experiment page where you can perform the experiment on POS Tagging.
		Befor performing the experiment, go through Procedure.

	Quizzess :
		This page gives you some questions on POS Tagging to practise for yourself.

	Procedure :
		This page tells you the procedure of the experiment> This page should be read before performing the experiment to know how the experiment works.

	Further Readings :
		This page gives you information for more materials to read about POS Tagging.

Experiment :
	First a drop-down box is given, which contains the Languages to select.
	On selecting the language, another drop-down with sentences is given.
	On selecting a sentence, a table is created with four columns. First column contains LEXICON, Second column, contains drop-down boxes with options filled in it to select.
	On selecting corresponding answers, click on Submit button.
	On clicking submit button, third column gets filled with status of your answers(correct or incorrect).
	On clicking Get Answers button, fourth column gets filled with corresponding answers.
	On clicking Hide Answers button, all answers in fourth column disappears.

Information on folders, files and database :
	run.py (file) :
		This files imports the other python files from app and runs the server on host.

	app (folder) :
		This folder contains all html, css, javascript files and python files.

	__init__.py (file) :
		This file initializes the app, and routes different pages to respective domains.

	sentenceselect.py (file) :
		This is python file which is responsible for smooth running of experiment in Experiment.html page.

	test.db (database) :
		This is database which contains all data required in experiment.

	templates (folder) :
		This folder contains all html files which are routed using flask (which searches files in templates folder).
	static (folder) :
		This folder contains all static files which are CSS files, JavaScript files, images, scripts, fonts.

	css (folder) :
		This contains all CSS files.

	js (folder) :
		This contains all JavaScript files.
	
	images (folder) :
		This contains all images.

	scripts (folder) :
		This contains all scripts.
