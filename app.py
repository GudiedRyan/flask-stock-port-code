from flask import Flask

app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return "Hello World!"

@app.route('/about',methods=['GET'])
def about():
    return '<h2>About this application...</h2>'

@app.route('/stocks/')
def stocks():
    return '<h2>Stock List...</h2>'