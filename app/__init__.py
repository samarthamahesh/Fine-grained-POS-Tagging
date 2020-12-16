'''
This python script routes to different pages.
'''
from flask import Flask, render_template
APP = Flask(__name__)

@APP.route('/')
def index_page():
    '''
    This function renders Introduction page.
    '''
    return render_template('Introduction.html'), 200

@APP.route('/Introduction.html')
def introduction():
    '''
    This function renders Introduction page.
    '''
    return render_template('Introduction.html'), 200

@APP.route('/Theory.html')
def theory():
    '''
    This function renders Theory page.
    '''
    return render_template('Theory.html'), 200

@APP.route('/Objective.html')
def objective():
    '''
    This function renders Objective page.
    '''
    return render_template('Objective.html'), 200

@APP.route('/Experiment.html')
def experiment():
    '''
    This function renders Experiment page.
    '''
    return render_template('Experiment.html'), 200

@APP.route('/Quizzes.html')
def quizzes():
    '''
    This function renders Quizzes page.
    '''
    return render_template('Quizzes.html'), 200

@APP.route('/Procedure.html')
def procedure():
    '''
    This function renders Procedure page.
    '''
    return render_template('Procedure.html'), 200

@APP.route('/Further_Readings.html')
def further_readings():
    '''
    This function renders Further Readings page.
    '''
    return render_template('Further_Readings.html'), 200

@APP.route('/Feedback.html')
def feedback():
    '''
    This function renders Feedback page.
    '''
    return render_template('Feedback.html'), 200
