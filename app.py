from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/user/<name>')
def hello(name):
    return '<h1>Hello!%s<h1><img src="http://helloflask.com/totoro.gif">'% name

@app.route('/test')
def test_url_for_():
    print(url_for('hello', name='Juno'))
    return 'Test page'