from flask import Flask, request
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

app = Flask(__name__, static_folder='images')

@app.route('/')
def home():
    return '<h1>home</h1>'

@app.route('/chart')
def chart():
    x = [1, 2, 3, 4, 5]
    y = [30, 21, 28, 21, 30]

    # virtual object
    figure = Figure()

    # physical object
    FigureCanvasAgg(figure)

    # adding a placeholder to add new chart
    chart = figure.add_subplot(1, 1, 1)

    # plot the x and y
    chart.plot(x, y)

    # save the plot/chart/graph to a file
    figure.savefig('./images/chart2.png')

    return '<h1>App Summary</h1><img src="/images/chart2.png">'

if __name__ == '__main__':
    app.run(debug=True, port=6600, host='0.0.0.0')

