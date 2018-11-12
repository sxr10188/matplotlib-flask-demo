#!/usr/bin/env python3

# https://stackoverflow.com/questions/50728328/python-how-to-show-matplotlib-in-flask

import os
import io
import random
from flask import Response,Flask, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


app = Flask(__name__)

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route("/plotpage")
def plotpage():
    return render_template('plotpage.html')

@app.route("/")
def homepage():
    return render_template('home.html')


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

if __name__=="__main__":
    port = port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
