from flask import Flask
app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome oooo'

@app.route('/members')
def members():
    return 'Welcome to Members only Live'
if __name__=='__main__':
    app.run(debug=True) 