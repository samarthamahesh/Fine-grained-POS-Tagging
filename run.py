'''
This python script runs the server.
'''
from app import APP, sentenceselect
if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5000, debug=True)
