'''
This python script is made for experiment  page
which handles everything in experiment page
'''
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from app import APP

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
DB = SQLAlchemy(APP)

class newAnswer(DB.Model):
    '''
    This class generates objects which contain id and an answer.
    '''
    id = DB.Column(DB.Integer, primary_key=True)
    answer = DB.Column(DB.String(1000))

    def __init__(self, answer):
        self.answer = answer

@APP.route('/addanswer', methods=['POST'])
def answer():
    '''
    This function adds answer into database
    '''
    ans = request.form['inputbox']
    DB.create_all()
    newAns = newAnswer(ans)
    DB.session.add(newAns)
    DB.session.commit()
    return render_template('Quizzes.html')

@APP.route('/lang', methods=['GET', 'POST'])
def langselect():
    '''
    This function takes which language is selected
    and returns the sentences of respective language.
    '''
    lang = request.form['dropddlang']
    if lang == '0':
        return render_template('Experiment.html')
    elif lang == '1':
        DB.create_all()
        cursor = DB.engine.execute('SELECT * FROM sentences')
        data = cursor.fetchall()
        return render_template('Experiment.html', showanswer=-1, data01=lang, data02=data)
    elif lang == '2':
        DB.create_all()
        cursor = DB.engine.execute('SELECT * FROM sentenceshin')
        data = cursor.fetchall()
        return render_template('Experiment.html', showanswer=-1, data01=lang, data02=data)

@APP.route('/sen', methods=['GET', 'POST'])
def senselect():
    '''
    This function takes sentennce which is selected and
    returns the words of that respective sentence to html page
    which is taken from database
    '''
    lang = request.form['hidlang']
    sen = request.form['dropddsen']
    if sen == '---Select a sentence---':
        return render_template('Experiment.html')
    else:
        DB.create_all()
        dataind = 0
        datalength = 0
        datasen1 = ''
        data = ''
        dataoptions = ''
        if lang == '1':
            cursor = DB.engine.execute('SELECT * FROM sentences WHERE SENTENCE = "' + sen + '"')
            dataind = cursor.fetchall()[0][0]
            cursor = DB.engine.execute('SELECT * FROM sentences WHERE SENTENCE = "' + sen + '"')
            datalength = int(cursor.fetchall()[0][2])
            cursor = DB.engine.execute("SELECT * FROM sen" + str(dataind))
            datasen1 = cursor.fetchall()
            cursor = DB.engine.execute('SELECT * FROM sentences')
            data = cursor.fetchall()
            cursor = DB.engine.execute('SELECT * FROM options')
            dataoptions = cursor.fetchall()
        elif lang == '2':
            cursor = DB.engine.execute('SELECT * FROM sentenceshin WHERE SENTENCE = "' + sen + '"')
            dataind = cursor.fetchall()[0][0]
            cursor = DB.engine.execute('SELECT * FROM sentenceshin WHERE SENTENCE = "' + sen + '"')
            datalength = int(cursor.fetchall()[0][2])
            cursor = DB.engine.execute("SELECT * FROM sen" + str(dataind) + 'hin')
            datasen1 = cursor.fetchall()
            cursor = DB.engine.execute('SELECT * FROM sentenceshin')
            data = cursor.fetchall()
            cursor = DB.engine.execute('SELECT * FROM optionshin')
            dataoptions = cursor.fetchall()
    return render_template('Experiment.html', showanswer=0, data11=sen, data12=dataind,
                           data13=datasen1, data01=lang, data02=data, data15=datalength,
                           dataopt=dataoptions)

@APP.route('/checkAnswers', methods=['GET', 'POST'])
def check():
    '''
    This function compares answers from html page with answers
    in database and returnns list containing 0's and 1's to print
    right or wrong mark
    '''
    checkans = request.form['hidans']
    lang = request.form['hidlang1']
    sen = request.form['hidsen']
    ind = request.form['hidind']
    senlen = int(request.form['hidlen'])
    DB.create_all()
    datasen = ''
    data = ''
    dataoptions = ''
    if lang == '1':
        cursor = DB.engine.execute('SELECT * FROM sen' + str(ind))
        datasen = cursor.fetchall()
        cursor = DB.engine.execute('SELECT * FROM sentences')
        data = cursor.fetchall()
        cursor = DB.engine.execute('SELECT * FROM options')
        dataoptions = cursor.fetchall()
    elif lang == '2':
        cursor = DB.engine.execute('SELECT * FROM sen' + str(ind) + 'hin')
        datasen = cursor.fetchall()
        cursor = DB.engine.execute('SELECT * FROM sentenceshin')
        data = cursor.fetchall()
        cursor = DB.engine.execute('SELECT * FROM optionshin')
        dataoptions = cursor.fetchall()
    dicti = []
    strtup = []
    for i in range(0, senlen):
        strind = str(i+1)
        string = request.form[strind]
        strtup.append(string)
        if datasen[i][2] == string:
            dicti.append('1')
        else:
            dicti.append('0')
    tup = tuple(dicti)
    strpass = tuple(strtup)
    if checkans == '1':
        return render_template('Experiment.html', showanswer=2,
                               data01=lang, data11=sen, data02=data, data12=ind, data15=senlen,
                               data2=tup, data13=datasen, data3=strpass, dataopt=dataoptions)
    else:
        return render_template('Experiment.html', showanswer=1,
                               data01=lang, data11=sen, data02=data, data12=ind, data15=senlen,
                               data2=tup, data13=datasen, data3=strpass, dataopt=dataoptions)
