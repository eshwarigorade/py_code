from flask import Flask

app = Flask(__name__)


@app.route('/')
def myFunction():
    return 'hello client!!!'

@app.route('/page1.html')
def respondPage1():
    return 'test page'

@app.route('/page2.html')
def respondPage2():
    return 'test page'

app.run()