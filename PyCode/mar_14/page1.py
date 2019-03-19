from flask import Flask, request

app = Flask(__name__)

# root
@app.route('/')
def homePage():
    return '<h1>Sunbeam</h1>'

@app.route('/add')
def addPage():
    p1 = 100
    p2 = 200
    answer = p1 + p2
    return '<h1>p1 + p2 = ' + str(answer) + '</h1>'

@app.route('/multiply')
def multiplyPage():
    # print(request.args)
    p1 = request.args['p1']
    p2 = request.args['p2']
    # print(p1, p2)
    result = int(p1) * int(p2)
    return '<h1>Multiplication: ' + str(result) + '</h1>'

@app.route('/ops')
def operationsPage():
    p1 = int(request.args['p1'])
    p2 = int(request.args['p2'])
    addition = p1 + p2
    multiplication = p1 * p2
    division = p1 / p2
    subtraction = p1 - p2
    # result = 'multiplication: {}<br/> addition: {}<br/> division: {}<br/> subtraction: {}'.format(multiplication, addition, division, subtraction)
    result = '<div>multiplication: {}</div><div>addition: {}</div><div>division: {}</div><div>subtraction: {}</div>'.format(multiplication, addition, division, subtraction)
    return result




if __name__ == '__main__':
    app.run()
