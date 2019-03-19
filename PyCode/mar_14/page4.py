from flask import Flask, request, render_template
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg


app = Flask(__name__, static_folder='images')

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ops')
def add():
    p1 = int(request.args['p1'])
    p2 = int(request.args['p2'])
    result = p1 + p2
    multiplication = p1 * p2
    return render_template('result.html', addition=result, multiplication=multiplication)

@app.route('/chart')
def chart():
    x = [1, 2, 3, 4, 5]
    y = [30, 20, 22, 20, 30]
    figure = Figure()
    FigureCanvasAgg(figure)
    chart = figure.add_subplot(1, 1, 1)
    chart.plot(x, y)
    figure.savefig('./images/chart3.png')
    return render_template('chart.html', fileName='/images/chart3.png')


if __name__ == '__main__':
    app.run(debug=True, port=6700, host='0.0.0.0')